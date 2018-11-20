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

from thoth.common import init_logging
from thoth.common import __version__ as __common__version__
from thoth.storages import GraphDatabase
from thoth.storages import SolverResultsStore
from thoth.storages import AnalysisResultsStore
from thoth.storages import __version__ as __storages__version__


__version__ = f"0.5.1+storage.{__storages__version__}.common.{__common__version__}"
__author__ = "Christoph Görn <goern@redhat.com>"

init_logging()
_LOGGER = logging.getLogger('thoth.graph_sync_job')

prometheus_registry = CollectorRegistry()

thoth_metrics_exporter_info = Gauge('graph_sync_job_info',
                                    'Thoth Graph Sync Job information', ['version'],
                                    registry=prometheus_registry)
thoth_metrics_exporter_info.labels(__version__).inc()

_THOTH_METRICS_PUSHGATEWAY_URL = os.getenv('THOTH_METRICS_PUSHGATEWAY_URL')
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


def sync_solver_documents(graph: GraphDatabase, document_ids: list = None, force: bool = False) -> None:
    """Sync solver documents into graph."""
    solver_store = SolverResultsStore(host=solver_results_store_host)
    solver_store.connect()

    for document_id in document_ids or solver_store.get_document_listing():
        _METRIC_SOLVER_RESULTS_PROCESSED.inc()

        if force or not graph.solver_document_id_exist(document_id):
            _LOGGER.info(
                f"Syncing solver document from {solver_store.ceph.host} "
                f"with id {document_id!r} to graph {graph.hosts}"
            )

            try:
                document = solver_store.retrieve_document(document_id)
                graph.sync_solver_result(document)
                _METRIC_SOLVER_RESULTS_SYNCED.inc()
            except Exception:
                _LOGGER.exception("Failed to sync solver result with document id %r", document_id)
                _METRIC_SOLVER_RESULTS_FAILED.inc()
        else:
            _LOGGER.info(f"Sync of solver document with id {document_id!r} skipped - already synced")
            _METRIC_SOLVER_RESULTS_SKIPPED.inc()


def sync_analysis_documents(graph: GraphDatabase, document_ids: list = None, force: bool = False) -> None:
    """Sync image analysis documents into graph."""
    analysis_store = AnalysisResultsStore(host=analysis_results_store_host)
    analysis_store.connect()

    for document_id in document_ids or analysis_store.get_document_listing():
        _METRIC_SOLVER_RESULTS_PROCESSED.inc()

        if force or not graph.analysis_document_id_exist(document_id):
            _LOGGER.info(
                f"Syncing analysis document from {analysis_store.ceph.host} "
                f"with id {document_id!r} to graph {graph.hosts}"
            )

            try:
                document = analysis_store.retrieve_document(document_id)
                graph.sync_analysis_result(document)
                _METRIC_SOLVER_RESULTS_SYNCED.inc()
            except Exception:
                _LOGGER.exception("Failed to sync analysis result with document id %r", document_id)
                _METRIC_SOLVER_RESULTS_FAILED.inc()
        else:
            _LOGGER.info(f"Sync of analysis document with id {document_id!r} skipped - already synced")
            _METRIC_SOLVER_RESULTS_SKIPPED.inc()


@click.command()
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
@click.option('-v', '--verbose', is_flag=True, envvar='THOTH_GRAPH_SYNC_DEBUG',
              help="Be more verbose about what's going on.")
@click.option('--force-sync', is_flag=True, envvar='THOTH_GRAPH_SYNC_FORCE_SYNC',
              help="Force sync of documents regardless if they exist (duplicate entries might not be created).")
@click.option('--metrics-pushgateway-url', type=str, default='pushgateway:80', show_default=True,
              envvar='THOTH_METRICS_PUSHGATEWAY_URL',
              help="Send job metrics to a Prometheus pushgateway URL.")
@click.option('--only-solver-documents', is_flag=True, envvar='THOTH_ONLY_SOLVER_DOCUMENTS', default=False,
              help="Sync only solver documents.")
@click.option('--only-analysis-documents', is_flag=True, envvar='THOTH_ONLY_ANALYSIS_DOCUMENTS', default=False,
              help="Sync only analysis documents.")
@click.argument('document-ids', envvar='THOTH_SYNC_DOCUMENT_ID', type=str, nargs=-1)
def cli(document_ids, verbose, force_sync, only_solver_documents, only_analysis_documents, metrics_pushgateway_url):
    """Sync analyses, inspection and solver results to the graph database."""
    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.debug('Debug mode is on')

    only_one_kind = sum((int(only_solver_documents), int(only_analysis_documents)))

    if only_one_kind > 1:
        _LOGGER.error("Cannot specify multiple --only-* options")
        return 1

    only_one_kind = bool(only_one_kind)

    if not only_one_kind and document_ids:
        _LOGGER.error(
            "Explicitly specified documents to be synced can be specified only with one of the --only-* options"
        )
        return 2

    graph = GraphDatabase()
    graph.connect()

    with _METRIC_SECONDS.time():
        if not only_one_kind or only_solver_documents:
            sync_solver_documents(graph, document_ids, force_sync)

        if not only_one_kind or only_analysis_documents:
            sync_analysis_documents(graph, document_ids, force_sync)

    if _THOTH_METRICS_PUSHGATEWAY_URL:
        try:
            _LOGGER.debug(f"Submitting metrics to Prometheus pushgateway {_THOTH_METRICS_PUSHGATEWAY_URL}")
            push_to_gateway(_THOTH_METRICS_PUSHGATEWAY_URL, job='graph-sync', registry=prometheus_registry)
        except Exception as e:
            _LOGGER.exception(f'An error occurred pushing the metrics: {str(e)}')


if __name__ == '__main__':
    _LOGGER.info(f"graph-sync-job v{__version__} starting...")
    cli()
