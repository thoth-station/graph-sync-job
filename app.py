#!/usr/bin/env python3
"""Graph syncing logic for the Thoth project."""

import logging

import click
from thoth.storages import GraphDatabase
from thoth.storages import SolverResultsStore

logging.basicConfig()
_LOGGER = logging.getLogger('thoth.graph_sync_job')


@click.group()
@click.option('-v', '--verbose', is_flag=True, envvar='THOTH_GRAPH_SYNC_DEBUG',
              help="Be more verbose about what's going on.")
def cli(verbose):
    """Graph syncing logic for the Thoth project."""
    logging.getLogger('thoth').setLevel(logging.DEBUG if verbose else logging.INFO)
    _LOGGER.debug('Debug mode is on')


@cli.command()
@click.option('--graph-hosts', type=str, default=[GraphDatabase.DEFAULT_HOST],
              show_default=True, metavar='HOST',
              envvar=GraphDatabase.ENVVAR_HOST_NAME, multiple=True,
              help="Hostname to the graph instance to perform sync to.")
@click.option('--graph-port', type=int, default=GraphDatabase.DEFAULT_PORT, show_default=True, metavar='HOST',
              envvar=GraphDatabase.ENVVAR_HOST_PORT,
              help="Port number to the graph instance to perform sync to.")
@click.option('--solver-results-store-host', type=str, show_default=True, metavar='HOST',
              envvar=SolverResultsStore.ENVVAR_HOST, default=SolverResultsStore.DEFAULT_HOST,
              help="Hostname to solver results store from which the sync should be performed.")
def sync(solver_results_store_host, graph_hosts, graph_port):
    graph = GraphDatabase(hosts=graph_hosts, port=graph_port)
    solver_store = SolverResultsStore(host=solver_results_store_host)

    _LOGGER.info(f"Syncing from {solver_results_store_host} to {graph_hosts}")
    for document_id, document in solver_store.iterate_results():
        _LOGGER.info(f"Syncing document with id {document_id!r} to graph")
        graph.store_pypi_solver_result(document_id, document)


if __name__ == '__main__':
    cli()
