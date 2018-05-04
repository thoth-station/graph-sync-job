#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from thoth.common import init_logging
from thoth.storages import GraphDatabase
from thoth.storages import SolverResultsStore
from thoth.storages import AnalysisResultsStore

init_logging()
_LOGGER = logging.getLogger('thoth.graph_sync_job')


@click.command()
@click.option('--graph-hosts', type=str, default=[GraphDatabase.DEFAULT_HOST],
              show_default=True, metavar=GraphDatabase.ENVVAR_HOST_NAME,
              envvar=GraphDatabase.ENVVAR_HOST_NAME, multiple=True,
              help="Hostname to the graph instance to perform sync to.")
@click.option('--graph-port', type=int, default=GraphDatabase.DEFAULT_PORT, show_default=True, metavar='HOST',
              envvar=GraphDatabase.ENVVAR_HOST_PORT,
              help="Port number to the graph instance to perform sync to.")
@click.option('--solver-results-store-host', type=str, show_default=True, metavar='HOST', default=None,
              help="Hostname to solver results store from which the sync should be performed.")
@click.option('--analysis-results-store-host', type=str, show_default=True, metavar='HOST', default=None,
              help="Hostname to analysis results store from which the sync should be performed.")
@click.option('-v', '--verbose', is_flag=True, envvar='THOTH_GRAPH_SYNC_DEBUG',
              help="Be more verbose about what's going on.")
@click.option('--force-solver-results-sync', is_flag=True, envvar='THOTH_GRAPH_SYNC_FORCE_SOLVER_RESULTS_SYNC',
              help="Force sync of solver results regardless if they exist (duplicate entries will not be created).")
@click.option('--force-analysis-results-sync', is_flag=True, envvar='THOTH_GRAPH_SYNC_FORCE_ANALYSIS_RESULTS_SYNC',
              help="Force sync of solver results regardless if they exist (duplicate entries will not be created).")
def cli(verbose, solver_results_store_host, analysis_results_store_host, graph_hosts, graph_port,
        force_solver_results_sync, force_analysis_results_sync):
    logging.getLogger('thoth').setLevel(
        logging.DEBUG if verbose else logging.INFO)
    _LOGGER.debug('Debug mode is on')

    graph = GraphDatabase(hosts=graph_hosts, port=graph_port)
    graph.connect()

    solver_store = SolverResultsStore(host=solver_results_store_host)
    solver_store.connect()

    _LOGGER.info(
        f"Syncing solver results from {solver_results_store_host} to {graph_hosts}")
    for document_id, document in solver_store.iterate_results():
        if force_solver_results_sync or not graph.solver_records_exist(document):
            _LOGGER.info(
                f"Syncing solver document with id {document_id!r} to graph")
            try:
                graph.sync_solver_result(document)
            except Exception:
                _LOGGER.exception(
                    "Failed to sync solver result with document id %r", document_id)
        else:
            _LOGGER.info(
                f"Sync of solver document with id {document_id!r} skipped - already synced")

    analysis_store = AnalysisResultsStore(host=analysis_results_store_host)
    analysis_store.connect()
    _LOGGER.info(f"Syncing image analysis results to {graph_hosts}")
    for document_id, document in analysis_store.iterate_results():
        if force_analysis_results_sync or not graph.analysis_records_exist(document):
            _LOGGER.info(
                f"Syncing analysis document with id {document_id!r} to graph")
            try:
                graph.sync_analysis_result(document)
            except Exception:
                _LOGGER.exception(
                    "Failed to sync analysis result with document id %r", document_id)
        else:
            _LOGGER.info(
                f"Sync of analysis document with id {document_id!r} skipped - already synced")


if __name__ == '__main__':
    cli()
