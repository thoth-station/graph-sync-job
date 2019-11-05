#!/usr/bin/env python3
# graph-sync-job
# Copyright(C) 2018, 2019 Fridolin Pokorny
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

import sys
import logging
import os
import time
from typing import List
from typing import Optional

import click

from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

from thoth.common import init_logging
from thoth.common import __version__ as __common__version__
from thoth.storages import __version__ as __storages__version__
from thoth.storages import sync_documents


__version__ = (
    f"0.6.0+thoth_storage.{__storages__version__}+thoth_common.{__common__version__}"
)


init_logging()
_LOGGER = logging.getLogger("thoth.graph_sync_job")

prometheus_registry = CollectorRegistry()

_THOTH_METRICS_PUSHGATEWAY_URL = os.getenv("PROMETHEUS_PUSHGATEWAY_URL")

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
    ["category", "namespace"],
    registry=prometheus_registry,
)
_METRIC_RESULTS_PROCESSED = Counter(
    "graph_sync_results_processed",
    "Results processed",
    ["category", "namespace"],
    registry=prometheus_registry,
)
_METRIC_RESULTS_SYNCED = Counter(
    "graph_sync_results_synced",
    "Results synced",
    ["category", "namespace"],
    registry=prometheus_registry,
)
_METRIC_RESULTS_SKIPPED = Counter(
    "graph_sync_results_skipped",
    "Results skipped processing",
    ["category", "namespace"],
    registry=prometheus_registry,
)
_METRIC_RESULTS_FAILED = Counter(
    "graph_sync_results_failed",
    "Results failed processing",
    ["category", "namespace"],
    registry=prometheus_registry,
)


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    # Reuse thoth-storages version as we rely on it.
    click.echo(__version__)
    ctx.exit()


def _do_sync(
    document_ids: Optional[List[str]],
    force_sync: bool,
    amun_api_url: Optional[str],
    inspection_only_graph_sync: bool,
    inspection_only_ceph_sync: bool,
    is_local: bool,
) -> None:
    """Perform actual sync of documents."""
    namespace = os.getenv("THOTH_NAMESPACE")
    if not namespace:
        _LOGGER.warning("Namespace variable not provided for %r", namespace)

    start_time = time.monotonic()
    stats = sync_documents(
        document_ids,
        force=force_sync,
        graceful=False,
        inspection_only_graph_sync=inspection_only_graph_sync,
        inspection_only_ceph_sync=inspection_only_ceph_sync,
        amun_api_url=amun_api_url,
        is_local=is_local,
    )
    sync_time = time.monotonic() - start_time

    for category, category_stats in stats.items():
        processed, synced, skipped, failed = category_stats
        _METRIC_SECONDS.labels(category=category, namespace=namespace).set(sync_time)
        _METRIC_RESULTS_PROCESSED.labels(category=category, namespace=namespace).inc(
            processed
        )
        _METRIC_RESULTS_SYNCED.labels(category=category, namespace=namespace).inc(
            synced
        )
        _METRIC_RESULTS_SKIPPED.labels(category=category, namespace=namespace).inc(
            skipped
        )
        _METRIC_RESULTS_FAILED.labels(category=category, namespace=namespace).inc(
            failed
        )


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
@click.option(
    "--local-file",
    is_flag=True,
    envvar="THOTH_SYNC_LOCAL_FILE",
    default=False,
    help="Sync results present on the local filesystem instead of using Ceph adapters to retrieve them.",
)
def cli(
    document_ids,
    verbose,
    force_sync,
    amun_api_url,
    inspection_only_graph_sync,
    inspection_only_ceph_sync,
    local_file,
):
    """Sync analyses, inspection and solver results to the graph database."""
    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.debug("Debug mode is on")

    _do_sync(
        document_ids=document_ids,
        force_sync=force_sync,
        amun_api_url=amun_api_url,
        inspection_only_graph_sync=inspection_only_graph_sync,
        inspection_only_ceph_sync=inspection_only_ceph_sync,
        is_local=local_file,
    )

    if _THOTH_METRICS_PUSHGATEWAY_URL:
        try:
            _LOGGER.debug(
                "Submitting metrics to Prometheus pushgateway %r",
                _THOTH_METRICS_PUSHGATEWAY_URL,
            )
            push_to_gateway(
                _THOTH_METRICS_PUSHGATEWAY_URL,
                job="graph-sync",
                registry=prometheus_registry,
            )
        except Exception as exc:
            _LOGGER.exception("An error occurred pushing the metrics: %s", str(exc))


if __name__ == "__main__":
    _LOGGER.info(f"graph-sync-job v{__version__} starting...")
    cli()
