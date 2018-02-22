#!/usr/bin/env python3
"""Graph syncing logic for the Thoth project."""

import logging

import click
#from thoth.storages import JanusGraphDatabase
#from thoth.storages import SolverResultsStore

logging.basicConfig()
_LOGGER = logging.getLogger('thoth.graph_sync_job')


@click.group()
@click.option('-v', '--verbose', is_flag=True, envvar='THOTH_GRAPH_SYNC_DEBUG',
              help="Be more verbose about what's going on.")
def cli(verbose):
    """Graph syncing logic for the Thoth project."""
    _LOGGER.setLevel(logging.DEBUG if verbose else logging.INFO)
    _LOGGER.debug('Debug mode is on')


@cli.command()
@click.option('--janusgraph-host', type=str, default='localhost:8182', show_default=True, metavar='HOST',
              envvar='THOTH_JANUSGRAPH_HOST',
              help="Hostname to the JanusGraph instance to perform sync to.")
@click.option('--solver-results-store', type=str, default='localhost', show_default=True, metavar='HOST',
              envvar='THOTH_SERVER_RESULTS_HOST',
              help="Hostname to solver results store from which the sync should be performed.")
def sync(solver_results_store, janusgraph_host):
    _LOGGER.info(f"Syncing from {solver_results_store} to {janusgraph_host}")


if __name__ == '__main__':
    cli()
