thoth-graph-sync-job
--------------------

.. image:: https://img.shields.io/github/v/tag/thoth-station/graph-sync-job?style=plastic
  :target: https://github.com/thoth-station/graph-sync-job/releases
  :alt: GitHub tag (latest by date)

.. image:: https://quay.io/repository/thoth-station/graph-sync-job/status
  :target: https://quay.io/repository/thoth-station/graph-sync-job?tab=tags
  :alt: Quay - Build

The graph sync job will read in all
`solver <https://github.com/thoth-station/solver>`_,
`package-analyzer <https://github.com/thoth-station/package-analyzer>`_,
`package-extract <https://github.com/thoth-station/package-extract>`_,
`adviser <https://github.com/thoth-station/adviser>`_,
`provenance-checker <https://github.com/thoth-station/adviser/blob/master/docs/source/provenance_checks.rst>`_,
`dependency-monkey <https://github.com/thoth-station/adviser/blob/master/docs/source/dependency_monkey.rst>`_ and
`inspection <https://github.com/thoth-station/amun-api>`_
documents and synchronize them to Thoth database. If a document has
been synchronized before, it will not be synchronized again (unless the
synchronization is forced). The graph sync job runs periodically based
on configuration of CronJob that can be found in this repository under the
`openshift/` directory.

Installation and Deployment
===========================

The CronJob is created using OpenShift templates present in the `openshift/`
directory that can be found in the root of this Git repository. The actual
deployment is done using Ansible playbooks present in the
`Thoth's core repository <https://github.com/thoth-station/core>`_. OpenShift's
Source-to-Image mechanism is used to run this Python3 application.
