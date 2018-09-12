.. Thoth's Software Stack (aka Graph) Synchronization Job for OpenShift documentation master file

Welcome to Thoth's Software Stack (aka Graph) Synchronization Job for OpenShift's documentation!
================================================================================================

The graph sync job will read in all Solver and Analyzer documents and synchronized them to the JanusGraph database. If a document has been synchronized before, it will not be synchronized again (unless the synchronization is forced). The graph sync job runs each hour, this could be reconfigured within the CronJob `graph-sync`.

Contents:

.. toctree::
    :maxdepth: 2

    observability
    CHANGELOG

.. todolist::


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

