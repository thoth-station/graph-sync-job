#!/usr/bin/env python3
# graph-sync-job
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Graph syncing logic for the Thoth project."""

import logging

import click

from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

from thoth.common import init_logging
from thoth.common import __version__ as __common__version__
from thoth.storages import __version__ as __storages__version__
from thoth.storages import sync_analysis_documents
from thoth.storages import sync_solver_documents
from thoth.storages import sync_inspection_documents


__version__ = f"0.5.3+storage.{__storages__version__}.common.{__common__version__}"


init_logging()
_LOGGER = logging.getLogger("thoth.graph_sync_job")

prometheus_registry = CollectorRegistry()

thoth_metrics_exporter_info = Gauge(
    "graph_sync_job_info",
    "Thoth Graph Sync Job information",
    ["version"],
    registry=prometheus_registry,
)
thoth_metrics_exporter_info.labels(__version__).inc()

_METRIC_SECONDS = Gauge(
    "graph_sync_job_runtime_seconds",
    "Runtime of graph sync job in seconds.",
    registry=prometheus_registry,
)

_METRIC_SOLVER_RESULTS_PROCESSED = Counter(
    "graph_sync_solver_results_processed",
    "Solver results processed",
    registry=prometheus_registry,
)
_METRIC_SOLVER_RESULTS_SYNCED = Counter(
    "graph_sync_solver_results_synced",
    "Solver results synced",
    registry=prometheus_registry,
)
_METRIC_SOLVER_RESULTS_SKIPPED = Counter(
    "graph_sync_solver_results_skipped",
    "Solver results skipped processing",
    registry=prometheus_registry,
)
_METRIC_SOLVER_RESULTS_FAILED = Counter(
    "graph_sync_solver_results_failed",
    "Solver results failed processing",
    registry=prometheus_registry,
)

_METRIC_ANALYSIS_RESULTS_PROCESSED = Counter(
    "graph_sync_analysis_results_processed",
    "Analysis results processed",
    registry=prometheus_registry,
)
_METRIC_ANALYSIS_RESULTS_SYNCED = Counter(
    "graph_sync_analysis_results_synced",
    "Analysis results synced",
    registry=prometheus_registry,
)
_METRIC_ANALYSIS_RESULTS_SKIPPED = Counter(
    "graph_sync_analysis_results_skipped",
    "Analysis results skipped processing",
    registry=prometheus_registry,
)
_METRIC_ANALYSIS_RESULTS_FAILED = Counter(
    "graph_sync_analysis_results_failed",
    "Analysis results failed processing",
    registry=prometheus_registry,
)


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    # Reuse thoth-storages version as we rely on it.
    click.echo(__version__)
    ctx.exit()


@click.command()
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    callback=_print_version,
    expose_value=False,
    help="Print version and exit.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    envvar="THOTH_GRAPH_SYNC_DEBUG",
    help="Be more verbose about what's going on.",
)
@click.option(
    "--metrics-pushgateway-url",
    type=str,
    default=None,
    required=False,
    envvar="THOTH_METRICS_PUSHGATEWAY_URL",
    help="Send job metrics to a Prometheus pushgateway URL.",
)
@click.option(
    "--only-solver-documents",
    is_flag=True,
    envvar="THOTH_ONLY_SOLVER_DOCUMENTS",
    default=False,
    help="Sync only solver documents.",
)
@click.option(
    "--only-analysis-documents",
    is_flag=True,
    envvar="THOTH_ONLY_ANALYSIS_DOCUMENTS",
    default=False,
    help="Sync only analysis documents.",
)
@click.option(
    "--only-inspection-documents",
    is_flag=True,
    envvar="THOTH_ONLY_INSPECTION_DOCUMENTS",
    default=False,
    help="Sync only inspection documents.",
)
@click.option(
    "--amun-api-url",
    type=str,
    envvar="AMUN_API_URL",
    default=None,
    help="Amun API url to retrieve inspections from.",
)
@click.option(
    "--force-sync",
    is_flag=True,
    envvar="THOTH_FORCE_SYNC",
    default=False,
    help="Force sync of analysis documents.",
)
@click.option(
    "--document-id",
    "document_ids",
    type=str,
    envvar="THOTH_SYNC_DOCUMENT_ID",
    multiple=True,
    help="Explicitly sync only the given document or documents.",
)
@click.option(
    "--inspection-only-graph-sync",
    is_flag=True,
    envvar="THOTH_SYNC_INSPECTION_ONLY_GRAPH",
    default=False,
    help="Sync inspection results only to graph database, omit Ceph.",
)
@click.option(
    "--inspection-only-ceph-sync",
    is_flag=True,
    envvar="THOTH_SYNC_INSPECTION_ONLY_CEPH",
    default=False,
    help="Sync inspection results only to Ceph database, omit graph database.",
)
def cli(
    document_ids,
    verbose,
    force_sync,
    amun_api_url,
    only_solver_documents,
    only_analysis_documents,
    only_inspection_documents,
    metrics_pushgateway_url,
    inspection_only_graph_sync,
    inspection_only_ceph_sync,
):
    """Sync analyses, inspection and solver results to the graph database."""
    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.debug("Debug mode is on")

    only_one_kind = sum(
        (
            int(only_solver_documents),
            int(only_analysis_documents),
            int(only_inspection_documents),
        )
    )

    if only_one_kind > 1:
        _LOGGER.error("There can be only one --only-* option specified")
        return 1

    only_one_kind = bool(only_one_kind)

    if not only_one_kind and document_ids:
        _LOGGER.error(
            "Explicitly specified documents to be synced can be specified only with one of the --only-* options"
        )
        return 2

    with _METRIC_SECONDS.time():
        if not only_one_kind or only_solver_documents:
            _LOGGER.info("Syncing solver results")
            _METRIC_SOLVER_RESULTS_PROCESSED, \
                _METRIC_SOLVER_RESULTS_SYNCED, \
                _METRIC_SOLVER_RESULTS_SKIPPED, \
                _METRIC_SOLVER_RESULTS_FAILED = sync_solver_documents(
                    document_ids, force_sync, graceful=False
                )

        if not only_one_kind or only_analysis_documents:
            _LOGGER.info("Syncing image analysis results")
            _METRIC_ANALYSIS_RESULTS_PROCESSED, \
                _METRIC_ANALYSIS_RESULTS_SYNCED, \
                _METRIC_ANALYSIS_RESULTS_SKIPPED, \
                _METRIC_ANALYSIS_RESULTS_FAILED = sync_analysis_documents(
                    document_ids, force_sync, graceful=False
                )

        if not only_one_kind or only_inspection_documents:
            _LOGGER.info("Syncing data from Amun API %r", amun_api_url)
            if not amun_api_url:
                _LOGGER.error(
                    "Cannot perform sync of Amun documents, no Amun API URL provided"
                )
                return 3
            sync_inspection_documents(
                amun_api_url,
                document_ids,
                force_sync=force_sync,
                graceful=False,
                only_ceph_sync=inspection_only_ceph_sync,
                only_graph_sync=inspection_only_graph_sync,
            )
        elif inspection_only_ceph_sync or inspection_only_graph_sync:
            _LOGGER.warning(
                "Inspection sync was not performed but --inspection-only-ceph-sync "
                "or --inspection-only-graph-sync flags were set"
            )

    if metrics_pushgateway_url:
        try:
            _LOGGER.debug(
                "Submitting metrics to Prometheus pushgateway %r",
                metrics_pushgateway_url,
            )
            push_to_gateway(
                metrics_pushgateway_url, job="graph-sync", registry=prometheus_registry
            )
        except Exception as exc:
            _LOGGER.exception("An error occurred pushing the metrics: %s", str(exc))


if __name__ == "__main__":
    _LOGGER.info(f"graph-sync-job v{__version__} starting...")

    cli()
