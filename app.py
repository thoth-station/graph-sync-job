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

import os
import logging

import click

from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

from amun import get_inspection_build_log
from amun import get_inspection_job_log
from amun import get_inspection_specification
from amun import get_inspection_status
from amun import is_inspection_finished
from amun import has_inspection_job

from thoth.common import init_logging
from thoth.common import __version__ as __common__version__
from thoth.storages import __version__ as __storages__version__
from thoth.storages import sync_analysis_documents
from thoth.storages import sync_solver_documents
from thoth.storages import DependencyMonkeyReportsStore
from thoth.storages import InspectionResultsStore


__version__ = f"0.5.1+storage.{__storages__version__}.common.{__common__version__}"
__author__ = "Christoph Görn <goern@redhat.com>"

init_logging()
_LOGGER = logging.getLogger('thoth.graph_sync_job')

prometheus_registry = CollectorRegistry()

thoth_metrics_exporter_info = Gauge('graph_sync_job_info',
                                    'Thoth Graph Sync Job information', ['version'],
                                    registry=prometheus_registry)
thoth_metrics_exporter_info.labels(__version__).inc()

_METRIC_SECONDS = Gauge(
    'graph_sync_job_runtime_seconds', 'Runtime of graph sync job in seconds.',
    registry=prometheus_registry)

_METRIC_SOLVER_RESULTS_PROCESSED = Counter(
    'graph_sync_solver_results_processed', 'Solver results processed',
    registry=prometheus_registry)
_METRIC_SOLVER_RESULTS_SYNCED = Counter(
    'graph_sync_solver_results_synced', 'Solver results synced',
    registry=prometheus_registry)
_METRIC_SOLVER_RESULTS_SKIPPED = Counter(
    'graph_sync_solver_results_skipped', 'Solver results skipped processing',
    registry=prometheus_registry)
_METRIC_SOLVER_RESULTS_FAILED = Counter(
    'graph_sync_solver_results_failed', 'Solver results failed processing',
    registry=prometheus_registry)

_METRIC_ANALYSIS_RESULTS_PROCESSED = Counter(
    'graph_sync_analysis_results_processed', 'Analysis results processed',
    registry=prometheus_registry)
_METRIC_ANALYSIS_RESULTS_SYNCED = Counter(
    'graph_sync_analysis_results_synced', 'Analysis results synced',
    registry=prometheus_registry)
_METRIC_ANALYSIS_RESULTS_SKIPPED = Counter(
    'graph_sync_analysis_results_skipped', 'Analysis results skipped processing',
    registry=prometheus_registry)
_METRIC_ANALYSIS_RESULTS_FAILED = Counter(
    'graph_sync_analysis_results_failed', 'Analysis results failed processing',
    registry=prometheus_registry)


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    # Reuse thoth-storages version as we rely on it.
    click.echo(__version__)
    ctx.exit()


def iterate_inspection_ids():
    """Iterate over inspection ids that were run."""
    reports_store = DependencyMonkeyReportsStore()
    reports_store.connect()

    for _, report in reports_store.iterate_results():
        # Yield inspections.
        yield from report['result']['output']


def sync_inspection_documents(amun_api_url: str, document_ids: list = None, force_sync: bool = False) -> None:
    """Sync observations made on Amun into graph databaes."""
    inspection_store = InspectionResultsStore()

    processed, synced, skipped, failed = 0, 0, 0, 0
    for document_id in document_ids or iterate_inspection_ids():
        processed += 1
        if force_sync or not graph.inspection_document_id_exist(document_id):
            if is_inspection_finished(amun_api_url, inspection_id):
                _LOGGER.info(f"Syncing inspection {inspection_id!r} to {inspection_store.ceph.host}")

                try:
                    specification = get_inspection_specification(amun_api_url, inspection_id)
                    build_log = get_inspection_build_log(amun_api_url, inspection_id)
                    status = get_inspection_status(amun_api_url, inspection_id)
                    job_log = None

                    if has_inspection_job(amun_api_url, inspection_id):
                        job_log = get_inspection_job_log(amun_api_url, inspection_id)

                    document = {
                        'specification': specification,
                        'build_log': build_log,
                        'job_log': job_log,
                        'inspection_id': inspection_id,
                        'status': status
                    }

                    # TODO: sync to GraphDatabase and mirror on ceph
                    inspection_store.store_document(document)
                    synced += 1
                except Exception as exc:
                    _LOGGER.exception(f"Failed to sync inspection %r: %s", inspection_id, str(exc))
                    failed += 1
            else:
                _LOGGER.info(f"Skipping inspection {inspection_id!r} - not finised yet")
                skipped += 1
        else:
            _LOGGER.info(f"Skipping inspection {inspection_id!r} - the given inspection is already synced")
            skipped += 1

    return processed, synced, skipped, failed

@click.command()
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
@click.option('-v', '--verbose', is_flag=True, envvar='THOTH_GRAPH_SYNC_DEBUG',
              help="Be more verbose about what's going on.")
@click.option('--force-solver-results-sync', is_flag=True, envvar='THOTH_GRAPH_SYNC_FORCE_SOLVER_RESULTS_SYNC',
              help="Force sync of solver results regardless if they exist (duplicate entries will not be created).")
@click.option('--force-analysis-results-sync', is_flag=True, envvar='THOTH_GRAPH_SYNC_FORCE_ANALYSIS_RESULTS_SYNC',
              help="Force sync of solver results regardless if they exist (duplicate entries will not be created).")
@click.option('--metrics-pushgateway-url', type=str, default='pushgateway:80', show_default=True,
              envvar='THOTH_METRICS_PUSHGATEWAY_URL',
              help="Send job metrics to a Prometheus pushgateway URL.")
@click.option('--only-solver-documents', is_flag=True, envvar='THOTH_ONLY_SOLVER_DOCUMENTS', default=False,
              help="Sync only solver documents.")
@click.option('--only-analysis-documents', is_flag=True, envvar='THOTH_ONLY_ANALYSIS_DOCUMENTS', default=False,
              help="Sync only analysis documents.")
@click.option('--only-inspection-documents', is_flag=True, envvar='THOTH_ONLY_INSPECTION_DOCUMENTS', default=False,
              help="Sync only inspection documents.")
@click.option('--amun-api-url', is_flag=True, envvar='AMUN_API_URL', default=False,
              help="Amun API url to retrieve inspections from.")
@click.argument('document-ids', envvar='THOTH_SYNC_DOCUMENT_ID', type=str, nargs=-1)
def cli(document_ids, verbose, force_sync, amun_api_url,
        only_solver_documents, only_analysis_documents, metrics_pushgateway_url):
    """Sync analyses, inspection and solver results to the graph database."""
    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.debug('Debug mode is on')

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
            _METRIC_SOLVER_RESULTS_FAILED = sync_solver_documents(document_ids, force_sync)

        if not only_one_kind or only_analysis_documents:
            _LOGGER.info("Syncing image analysis results")
            _METRIC_ANALYSIS_RESULTS_PROCESSED, \
            _METRIC_ANALYSIS_RESULTS_SYNCED, \
            _METRIC_ANALYSIS_RESULTS_SKIPPED, \
            _METRIC_ANALYSIS_RESULTS_FAILED = sync_analysis_documents(document_ids, force_sync)

        if amun_api_url:
            _LOGGER.info("Syncing data from Amun API")
            if not only_one_kind or only_inspection_documents:
                # TODO: add metrics
                sync_inspection_documents(amun_api_url, document_ids, force_sync)
        else:
            _LOGGER.info("Amun results skipped as Amun API URL was not provided")

    if metrics_pushgateway_url:
        try:
            _LOGGER.debug("Submitting metrics to Prometheus pushgateway %r", metrics_pushgateway_url)
            push_to_gateway(metrics_pushgateway_url, job='graph-sync', registry=prometheus_registry)
        except Exception as e:
            _LOGGER.exception('An error occurred pushing the metrics: %s', str(exc))


if __name__ == '__main__':
    _LOGGER.info(f"graph-sync-job v{__version__} starting...")

    cli()
