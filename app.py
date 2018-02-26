#!/usr/bin/env python3
"""Graph syncing logic for the Thoth project."""

import logging

import click
from thoth.storages import JanusGraphDatabase
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
@click.option('--janusgraph-hosts', type=str, default=[JanusGraphDatabase.DEFAULT_HOST],
              show_default=True, metavar='HOST',
              envvar=JanusGraphDatabase.ENVVAR_HOST_NAME, multiple=True,
              help="Hostname to the JanusGraph instance to perform sync to.")
@click.option('--janusgraph-port', type=int, default=JanusGraphDatabase.DEFAULT_PORT, show_default=True, metavar='HOST',
              envvar=JanusGraphDatabase.ENVVAR_HOST_PORT,
              help="Port number to the JanusGraph instance to perform sync to.")
@click.option('--solver-results-store-host', type=str, show_default=True, metavar='HOST',
              envvar=SolverResultsStore.ENVVAR_HOST, default=SolverResultsStore.DEFAULT_HOST,
              help="Hostname to solver results store from which the sync should be performed.")
def sync(solver_results_store_host, janusgraph_hosts, janusgraph_port):
    janus_graph = JanusGraphDatabase(hosts=janusgraph_hosts, port=janusgraph_port)
    solver_store = SolverResultsStore(host=solver_results_store_host)

    _LOGGER.info(f"Syncing from {solver_results_store_host} to {janusgraph_hosts}")
    for document_id, document in solver_store.iterate_results():
        _LOGGER.info(f"Syncing document with id {document_id!r} to JanusGraph")
        janus_graph.store_pypi_solver_result(document_id, document)


if __name__ == '__main__':
    cli()
