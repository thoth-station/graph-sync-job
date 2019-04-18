thoth-graph-sync-job
--------------------

The graph sync job will read in all
`solver <https://github.com/thoth-station/solver>`_ and
`package-extract <https://github.com/thoth-station/package-extract>`_
documents and synchronize them to the Dgraph database. If a document has
been synchronized before, it will not be synchronized again (unless the
synchronization is forced). The graph sync job runs runs periodically based
on configuration of CronJob that can be found in this repository under the
`openshift/` directory.

Installation and Deployment
===========================

The CronJob is created using OpenShift templates present in the `openshift/`
directory that can be found in the root of this Git repository. The actual
deployment is done using Ansible playbooks present in the
`Thoth's core repository <https://github.com/thoth-station/core>`_. OpenShift's
Source-to-Image mechanism is used to run this Python3 application.
