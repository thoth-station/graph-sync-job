# Changelog

## [0.5.0] - 2018-Sep-10 - goern

### Added

- added some docs, sphinx, Makefile for `make html`, the HTML docs can be found in `_build/html`
- now sending metrics to a Prometheus push gateway

## [0.4.0] - 2018-Jul-02 - goern

### Added

Starting with this release we have a Zuul-CI pipeline that:

- lints on Pull Requrest and gate/merge

## [0.3.0] - 2018-Jun-12 - goern

### Added

Set resource limits of BuildConfig and Deployment to reasonable values, this will prevent unpredicted behavior on UpShift.

## Release 0.6.1 (2020-05-18T11:24:38)
* all the github standard templates
* :sparkles: pre-commit installed and used it to do some reformatting
* :sparkles: added a __service_version__ and refactored __version__ so that it can be maintained by Kebechet
* :pushpin: Automatic update of dependency thoth-storages from 0.22.9 to 0.22.10
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic update of dependency thoth-common from 0.13.1 to 0.13.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.8 to 0.22.9
* :pushpin: Automatic update of dependency thoth-common from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency click from 7.1.1 to 7.1.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.7 to 0.22.8
* :pushpin: Automatic update of dependency thoth-common from 0.12.10 to 0.13.0
* :pushpin: Automatic update of dependency thoth-common from 0.12.9 to 0.12.10
* :pushpin: Automatic update of dependency autopep8 from 1.5.1 to 1.5.2
* :pushpin: Automatic update of dependency thoth-common from 0.12.8 to 0.12.9
* :pushpin: Automatic update of dependency thoth-common from 0.12.7 to 0.12.8
* Remove latest version restriction from .thoth.yaml
* :pushpin: Automatic update of dependency thoth-common from 0.12.6 to 0.12.7
* :pushpin: Automatic update of dependency autopep8 from 1.5 to 1.5.1
* :pushpin: Automatic update of dependency thoth-common from 0.12.5 to 0.12.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.4 to 0.12.5
* Add WorkflowTemplate for graph-sync to the correct location
* :pushpin: Automatic update of dependency thoth-storages from 0.22.6 to 0.22.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.5 to 0.22.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.3 to 0.12.4
* :pushpin: Automatic update of dependency thoth-common from 0.12.2 to 0.12.3
* :pushpin: Automatic update of dependency thoth-common from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency thoth-common from 0.12.0 to 0.12.1
* :pushpin: Automatic update of dependency thoth-common from 0.10.12 to 0.12.0
* :pushpin: Automatic update of dependency thoth-storages from 0.22.4 to 0.22.5
* :pushpin: Automatic update of dependency thoth-storages from 0.22.3 to 0.22.4
* :pushpin: Automatic update of dependency thoth-common from 0.10.11 to 0.10.12
* :pushpin: Automatic update of dependency thoth-common from 0.10.9 to 0.10.11
* :pushpin: Automatic update of dependency thoth-common from 0.10.9 to 0.10.11
* :pushpin: Automatic update of dependency click from 7.0 to 7.1.1
* :pushpin: Automatic update of dependency click from 7.0 to 7.1.1
* :pushpin: Automatic update of dependency thoth-common from 0.10.8 to 0.10.9
* :pushpin: Automatic update of dependency thoth-storages from 0.22.2 to 0.22.3
* :pushpin: Automatic update of dependency thoth-common from 0.10.7 to 0.10.8
* :pushpin: Automatic update of dependency thoth-common from 0.10.6 to 0.10.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.1 to 0.22.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.5 to 0.10.6
* :pushpin: Automatic update of dependency thoth-storages from 0.22.0 to 0.22.1
* :pushpin: Automatic update of dependency thoth-storages from 0.21.11 to 0.22.0
* Update .thoth.yaml
* :pushpin: Automatic update of dependency thoth-common from 0.10.4 to 0.10.5
* :pushpin: Automatic update of dependency thoth-common from 0.10.3 to 0.10.4
* :pushpin: Automatic update of dependency thoth-common from 0.10.2 to 0.10.3
* :pushpin: Automatic update of dependency thoth-common from 0.10.1 to 0.10.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency thoth-common from 0.9.31 to 0.10.0
* Update dependencies
* Update dependencies
* :pushpin: Automatic update of dependency thoth-common from 0.9.30 to 0.9.31
* :pushpin: Automatic update of dependency thoth-storages from 0.21.10 to 0.21.11
* :pushpin: Automatic update of dependency thoth-common from 0.9.29 to 0.9.30
* :pushpin: Automatic update of dependency thoth-storages from 0.21.9 to 0.21.10
* :pushpin: Automatic update of dependency thoth-storages from 0.21.8 to 0.21.9
* :pushpin: Automatic update of dependency thoth-common from 0.9.28 to 0.9.29
* :pushpin: Automatic update of dependency thoth-storages from 0.21.7 to 0.21.8
* :pushpin: Automatic update of dependency autopep8 from 1.4.4 to 1.5
* :pushpin: Automatic update of dependency thoth-common from 0.9.27 to 0.9.28
* :pushpin: Automatic update of dependency thoth-common from 0.9.26 to 0.9.27
* :pushpin: Automatic update of dependency thoth-storages from 0.21.6 to 0.21.7
* :pushpin: Automatic update of dependency thoth-common from 0.9.25 to 0.9.26
* :pushpin: Automatic update of dependency thoth-storages from 0.21.5 to 0.21.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.24 to 0.9.25
* :pushpin: Automatic update of dependency thoth-storages from 0.21.4 to 0.21.5
* :pushpin: Automatic update of dependency thoth-storages from 0.21.3 to 0.21.4
* :pushpin: Automatic update of dependency thoth-storages from 0.21.2 to 0.21.3
* :pushpin: Automatic update of dependency thoth-storages from 0.21.1 to 0.21.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.23 to 0.9.24
* :pushpin: Automatic update of dependency thoth-storages from 0.21.0 to 0.21.1
* :pushpin: Automatic update of dependency thoth-storages from 0.20.6 to 0.21.0
* :pushpin: Automatic update of dependency thoth-storages from 0.20.5 to 0.20.6
* Do not run adviser from bc in debug mode
* :pushpin: Automatic update of dependency thoth-common from 0.9.22 to 0.9.23
* :pushpin: Automatic update of dependency thoth-storages from 0.20.4 to 0.20.5
* :pushpin: Automatic update of dependency thoth-storages from 0.20.3 to 0.20.4
* :pushpin: Automatic update of dependency thoth-storages from 0.20.2 to 0.20.3
* :pushpin: Automatic update of dependency thoth-storages from 0.20.1 to 0.20.2
* Happy new year!
* :pushpin: Automatic update of dependency thoth-storages from 0.20.0 to 0.20.1
* :pushpin: Automatic update of dependency thoth-storages from 0.19.30 to 0.20.0
* :pushpin: Automatic update of dependency thoth-storages from 0.19.27 to 0.19.30
* :pushpin: Automatic update of dependency thoth-common from 0.9.21 to 0.9.22
* Use RHEL instead of UBI
* Update Thoth configuration file and Thoth's s2i configuration
* :pushpin: Automatic update of dependency thoth-storages from 0.19.26 to 0.19.27
* :pushpin: Automatic update of dependency thoth-storages from 0.19.25 to 0.19.26
* :pushpin: Automatic update of dependency thoth-common from 0.9.20 to 0.9.21
* :pushpin: Automatic update of dependency thoth-common from 0.9.19 to 0.9.20
* :pushpin: Automatic update of dependency thoth-common from 0.9.17 to 0.9.19
* :pushpin: Automatic update of dependency thoth-storages from 0.19.24 to 0.19.25
* :pushpin: Automatic update of dependency thoth-common from 0.9.16 to 0.9.17
* :pushpin: Automatic update of dependency thoth-storages from 0.19.23 to 0.19.24
* :pushpin: Automatic update of dependency thoth-storages from 0.19.22 to 0.19.23
* :pushpin: Automatic update of dependency thoth-storages from 0.19.21 to 0.19.22
* :pushpin: Automatic update of dependency thoth-storages from 0.19.19 to 0.19.21
* :pushpin: Automatic update of dependency thoth-common from 0.9.15 to 0.9.16
* :pushpin: Automatic update of dependency thoth-common from 0.9.14 to 0.9.15
* :pushpin: Automatic update of dependency thoth-storages from 0.19.18 to 0.19.19
* :pushpin: Automatic update of dependency thoth-storages from 0.19.17 to 0.19.18
* Manual update of dependencies
* :pushpin: Automatic update of dependency thoth-storages from 0.19.15 to 0.19.17
* Increase backoff limit for failing graph syncs
* just a new version 👅
* Create configuration option to explictly state documents are from a local dir
* :pushpin: Automatic update of dependency thoth-storages from 0.19.14 to 0.19.15
* Remove ttl configuration for cleanup
* Document-id provided to the graph-sync-job
* :pushpin: Automatic update of dependency thoth-storages from 0.19.13 to 0.19.14
* :pushpin: Automatic update of dependency thoth-storages from 0.19.12 to 0.19.13
* Template metadata label graph-sync-type is not required
* Adjust graph-sync-types where needed
* Fix referencing graph sync types.
* updated templates with annotations and param thoth-advise-value
* :pushpin: Automatic update of dependency thoth-storages from 0.19.11 to 0.19.12
* :pushpin: Automatic update of dependency thoth-storages from 0.19.10 to 0.19.11
* :fire: Hotfix for the var force_sync
* :pushpin: Automatic update of dependency thoth-storages from 0.19.9 to 0.19.10
* :pushpin: Automatic update of dependency thoth-common from 0.9.12 to 0.9.14
* :pushpin: Automatic update of dependency thoth-common from 0.9.11 to 0.9.12
* :pushpin: Automatic update of dependency thoth-common from 0.9.10 to 0.9.11
* Adjust deployment templates
* Simplify handling of syncs
* :pushpin: Automatic update of dependency thoth-storages from 0.19.8 to 0.19.9
* :pushpin: Automatic update of dependency thoth-storages from 0.19.7 to 0.19.8
* :pushpin: Automatic update of dependency thoth-storages from 0.19.6 to 0.19.7
* use postgresql hostname from thoth configmap
* Update thoth-python quickly
* Add label to distinguish adviser graph syncs
* :pushpin: Automatic update of dependency thoth-storages from 0.19.5 to 0.19.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.9 to 0.9.10
* :pushpin: Automatic update of dependency thoth-storages from 0.19.4 to 0.19.5
* :pushpin: Automatic update of dependency thoth-common from 0.9.8 to 0.9.9
* :pushpin: Automatic update of dependency thoth-storages from 0.19.3 to 0.19.4
* :pushpin: Automatic update of dependency thoth-storages from 0.19.2 to 0.19.3
* :pushpin: Automatic update of dependency thoth-storages from 0.19.1 to 0.19.2
* :pushpin: Automatic update of dependency thoth-storages from 0.19.0 to 0.19.1
* Updated the README
* :pushpin: Automatic update of dependency thoth-storages from 0.18.6 to 0.19.0
* Use more generic env var names
* Switch from Dgraph to PostgreSQL in deployment
* Start using Thoth's s2i base image
* :pushpin: Automatic update of dependency thoth-storages from 0.18.5 to 0.18.6
* Added config
* :pushpin: Automatic update of dependency thoth-common from 0.9.7 to 0.9.8
* :pushpin: Automatic update of dependency thoth-common from 0.9.6 to 0.9.7
* Remove old .thoth.yaml configuration file
* :pushpin: Automatic update of dependency thoth-storages from 0.18.4 to 0.18.5
* Change name of Thoth template to make Coala happy
* Start using Thoth in OpenShift's s2i
* :pushpin: Automatic update of dependency recommonmark from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency thoth-storages from 0.18.3 to 0.18.4
* :pushpin: Automatic update of dependency thoth-common from 0.9.5 to 0.9.6
* :pushpin: Automatic update of dependency thoth-storages from 0.18.1 to 0.18.3
* :pushpin: Automatic update of dependency thoth-storages from 0.18.0 to 0.18.1
* Standardize labels for metrics
* :pushpin: Automatic update of dependency thoth-storages from 0.17.0 to 0.18.0
* thoth-infra-stage is back
* deleted THOTH_SYNC_OBSERVATIONS from all templates
* added package analyzer to readme
* renamed from package-analysis to  package-analyzer
* added thoth-test-core
* Add Package-Analyzer Job Template and some changes
* Correct variable
* Fix template for dependency monkey graph sync job
* :pushpin: Automatic update of dependency thoth-storages from 0.16.0 to 0.17.0
* Readme typo
* :pushpin: Automatic update of dependency thoth-storages from 0.15.2 to 0.16.0
* Add monotonic time to avoid unexpected behavior when trying to measure durations
* Added namespace label
* Added time
* :pushpin: Automatic dependency re-locking
* syncing package analyzer results
* :pushpin: Automatic update of dependency thoth-storages from 0.15.1 to 0.15.2
* :pushpin: Automatic update of dependency thoth-storages from 0.15.0 to 0.15.1
* :pushpin: Automatic update of dependency thoth-storages from 0.14.8 to 0.15.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.3 to 0.9.4
* Fix syntax error
* Ignore GitHub markdown files in Coala
* Add CODEOWNERS file and standard GitHub templates
* Delete old metrics
* Added missing metrics and corrected wrong ones
* :pushpin: Automatic update of dependency thoth-storages from 0.14.7 to 0.14.8
* :pushpin: Automatic update of dependency thoth-common from 0.9.2 to 0.9.3
* :pushpin: Automatic update of dependency thoth-storages from 0.14.6 to 0.14.7
* :pushpin: Automatic update of dependency thoth-common from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency thoth-storages from 0.14.5 to 0.14.6
* :pushpin: Automatic update of dependency thoth-storages from 0.14.4 to 0.14.5
* :pushpin: Automatic update of dependency thoth-storages from 0.14.3 to 0.14.4
* Introduce retry mechanism for job
* Introduce template for graph sync multiple
* Corrected wrong attributes
* Fix syntax and undefined variable errors
* :pushpin: Automatic update of dependency thoth-storages from 0.14.2 to 0.14.3
* Increase backoff limit for syncs due to transactions
* Modify metrics so we can track time spent for graph-sync for each category (adviser, solver, dependency-monkey, inspection, package-extract, provenance-checker)
* Add missing import
* :pushpin: Automatic update of dependency thoth-storages from 0.14.1 to 0.14.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.0 to 0.9.1
* :pushpin: Automatic update of dependency prometheus-client from 0.7.0 to 0.7.1
* Let cleanup job clean all graph syncs after 1 hour
* Standardize variables and explicitly set the collection of metrics
* :pushpin: Automatic update of dependency thoth-common from 0.8.11 to 0.9.0
* Update zuul pipeline to use the new version trigger build job
* :pushpin: Automatic update of dependency prometheus-client from 0.6.0 to 0.7.0
* :pushpin: Automatic update of dependency thoth-common from 0.8.7 to 0.8.11
* :pushpin: Automatic update of dependency thoth-storages from 0.14.0 to 0.14.1
* :pushpin: Automatic update of dependency thoth-storages from 0.11.4 to 0.14.0
* :pushpin: Automatic update of dependency thoth-common from 0.8.5 to 0.8.7
* :pushpin: Automatic update of dependency thoth-storages from 0.11.3 to 0.11.4
* :pushpin: Automatic update of dependency thoth-storages from 0.11.2 to 0.11.3
* :pushpin: Automatic update of dependency thoth-storages from 0.11.1 to 0.11.2
* Fix check when syncing provenance checker documents
* Always issue force sync in the cluster
* :pushpin: Automatic update of dependency thoth-storages from 0.11.0 to 0.11.1
* :sparkles: added the correct zuul project queue
* :pushpin: Automatic update of dependency thoth-storages from 0.10.0 to 0.11.0
* Adjust graph-sync-job of solver documents for Dgraph
* Adjust graph-sync for provenance-checker
* Adjust graph-sync-job for package-extract
* Adjust graph-sync-job for inspections to use Dgraph
* Adjust adviser graph-sync-job template for Dgraph
* Remove JanusGraph specific bits
* :pushpin: Automatic update of dependency thoth-storages from 0.9.7 to 0.10.0
* Provide job for syncing dependency monkey documents
* :pushpin: Automatic update of dependency autopep8 from 1.4.3 to 1.4.4
* :pushpin: Automatic update of dependency thoth-common from 0.8.4 to 0.8.5
* Automatic update of dependency thoth-common from 0.8.3 to 0.8.4
* Automatic update of dependency thoth-common from 0.8.2 to 0.8.3
* Automatic update of dependency thoth-common from 0.8.1 to 0.8.2
* :sparkles: added ImageStream namespace and tag
* :sparkles: we dont need no swapping files
* :bug: fixed webhhok url
* Automatic update of dependency thoth-storages from 0.9.6 to 0.9.7
* Add Thoth's configuration file
* Automatic update of dependency thoth-common from 0.7.1 to 0.8.1
* Automatic update of dependency prometheus-client from 0.5.0 to 0.6.0
* Clean up syncs, let sync jobs be present for at least one hour
* Introduce graph-sync-provenance-checker
* Automatic update of dependency thoth-common from 0.6.0 to 0.7.1
* Automatic update of dependency thoth-storages from 0.9.5 to 0.9.6
* Add graph-sync-type to labels for sync type specific queries
* Automatic update of dependency sphinx-rtd-theme from 0.4.2 to 0.4.3
* Correctly error out if there are some issues
* It's already 2019
* Implement adviser documents syncing logic in graph syncs
* Introduce template for adviser graph syncs
* Automatic update of dependency thoth-common from 0.5.0 to 0.6.0
* Provide warning messages for better debugging
* Give inspection syncs ability to omit Ceph or graph database
* Give sync 2 hours, restart it if not finished
* Propagate document ids down to pods
* Add job identifier into templates
* Do not be graceful with syncs
* Automatic update of dependency recommonmark from 0.4.0 to 0.5.0
* Remove unused import
* Track document id in graph-sync jobs
* Fix generate name in template
* Revert "renamed the templates, as the ansible cronjob role expects the templates to be called ...-cronjob"
* renamed the templates, as the ansible cronjob role expects the templates to be called ...-cronjob
* Automatic update of dependency thoth-storages from 0.9.4 to 0.9.5
* Be graceful with inspection documents syncing
* Report Amun API into logs
* Automatic update of dependency thoth-common from 0.4.6 to 0.5.0
* Automatic update of dependency thoth-storages from 0.9.3 to 0.9.4
* Automatic update of dependency prometheus-client from 0.4.2 to 0.5.0
* Fix CI
* Move from argument to option so click handles env vars correctly
* Fix syncing of amun documents
* Move from cronjob to event driven jobs
* Use black for formatting
* Automatic update of dependency thoth-storages from 0.9.0 to 0.9.3
* Automatic update of dependency thoth-common from 0.4.5 to 0.4.6
* Automatic update of dependency thoth-storages from 0.8.0 to 0.9.0
* Automatic update of dependency thoth-common from 0.4.4 to 0.4.5
* Fix CI failures
* Move inspection sync to storages
* Sync inspection documents into graph database
* Be graceful with syncs
* Add more logging
* Sync onto Ceph
* Move syncing logic to storages
* Revert "Rewrite graph sync"
* Rewrite graph sync
* Automatic update of dependency thoth-common from 0.4.3 to 0.4.4
* Automatic update of dependency thoth-common from 0.4.2 to 0.4.3
* Automatic update of dependency thoth-common from 0.4.1 to 0.4.2
* Print source and destination per each file
* Automatic update of dependency thoth-common from 0.4.0 to 0.4.1
* Automatic update of dependency thoth-storages from 0.7.6 to 0.8.0
* Automatic update of dependency autopep8 from 1.4.2 to 1.4.3
* added _info metric to carry versions
* Print source and destination targets
* Automatic update of dependency thoth-storages from 0.7.5 to 0.7.6
* Automatic update of dependency thoth-storages from 0.7.4 to 0.7.5
* Automatic update of dependency thoth-storages from 0.7.3 to 0.7.4
* Automatic update of dependency thoth-storages from 0.7.2 to 0.7.3
* added _info metric to carry versions
* Automatic update of dependency thoth-common from 0.3.16 to 0.4.0
* Automatic update of dependency thoth-storages from 0.7.1 to 0.7.2
* Automatic update of dependency thoth-storages from 0.7.0 to 0.7.1
* Update thoth-common and thoth-storages packages
* Automatic update of dependency thoth-common from 0.3.14 to 0.3.15
* Automatic update of dependency thoth-common from 0.3.13 to 0.3.14
* Automatic update of dependency thoth-common from 0.3.12 to 0.3.13
* Update .zuul.yaml
* bounced version
* some cleanup, and using THOTH_S3_ENDPOINT_URL as default for solver_results_store_host and analysis_results_store_host
* Automatic update of dependency autopep8 from 1.4.1 to 1.4.2
* Automatic update of dependency thoth-storages from 0.5.4 to 0.6.0
* Automatic update of dependency thoth-common from 0.3.11 to 0.3.12
* Automatic update of dependency autopep8 from 1.4 to 1.4.1
* Automatic update of dependency prometheus-client from 0.4.1 to 0.4.2
* added SENTRY_DSN envvar and removed JANUSGRAPH
* Automatic update of dependency thoth-storages from 0.5.3 to 0.5.4
* Automatic update of dependency thoth-storages from 0.5.2 to 0.5.3
* Automatic update of dependency thoth-common from 0.3.10 to 0.3.11
* Automatic update of dependency thoth-common from 0.3.9 to 0.3.10
* Automatic update of dependency thoth-common from 0.3.8 to 0.3.9
* Automatic update of dependency thoth-common from 0.3.7 to 0.3.8
* Automatic update of dependency prometheus-client from 0.4.0 to 0.4.1
* Automatic update of dependency thoth-common from 0.3.6 to 0.3.7
* Automatic update of dependency sphinx-rtd-theme from 0.4.1 to 0.4.2
* Automatic update of dependency prometheus-client from 0.3.1 to 0.4.0
* Automatic update of dependency thoth-common from 0.3.5 to 0.3.6
* Update README file
* Automatic update of dependency thoth-common from 0.3.2 to 0.3.5
* Automatic update of dependency thoth-common from 0.3.1 to 0.3.2
* Automatic update of dependency click from 6.7 to 7.0
* Automatic update of dependency thoth-common from 0.3.0 to 0.3.1
* Fix deployment issues
* renamed metrics
* bounced version, fixed typos
* some more docs
* Counter has no labels?!
* fixed missing import of Counter
* added THOTH_FRONTEND_NAMESPACE configuration to ENV
* minor doc tweaks
* fixed coala issues
* relocked
* added _build/ as its a tmp artifact
* added what we need for sphinx
* added metrics to the graph sync job, so that we can observe if a document was processed, the sync failed, was skipped or was succesful synced
* removed stuff we dont need to ignore anymore
* fixed formating
* Automatic update of dependency thoth-common from 0.2.7 to 0.3.0
* Automatic update of dependency thoth-common from 0.2.6 to 0.2.7
* Automatic update of dependency thoth-common from 0.2.5 to 0.2.6
* Automatic update of dependency thoth-storages from 0.5.1 to 0.5.2
* Automatic update of dependency thoth-common from 0.2.4 to 0.2.5
* Automatic update of dependency thoth-common from 0.2.3 to 0.2.4
* build trigger
* Automatic update of dependency thoth-common from 0.2.2 to 0.2.3
* Automatic update of dependency thoth-storages from 0.5.0 to 0.5.1
* Automatic update of dependency thoth-storages from 0.4.0 to 0.5.0
* Automatic update of dependency thoth-storages from 0.3.0 to 0.4.0
* Automatic update of dependency thoth-storages from 0.2.0 to 0.3.0
* Automatic update of dependency thoth-storages from 0.1.1 to 0.2.0
* Add metadata to job template
* Add labels to job
* Automatic update of dependency thoth-common from 0.2.1 to 0.2.2
* Automatic update of dependency thoth-storages from 0.1.0 to 0.1.1
* Template default parameter fix
* Template default parameter fix
* Template default parameter fix
* Adjust template labels
* Introduce graph suspend configuration
* Automatic update of dependency thoth-storages from 0.0.33 to 0.1.0
* Automatic update of dependency thoth-common from 0.2.0 to 0.2.1
* Automatic update of dependency thoth-common from 0.2.0 to 0.2.1
* Automatic update of dependency thoth-common from 0.2.0 to 0.2.1
* Initial dependency lock
* Delete Pipfile.lock for relocking dependencies
* Update .zuul.yaml
* Automatic update of dependency thoth-common from 0.1.0 to 0.2.0
* Automatic update of dependency thoth-common from 0.0.9 to 0.1.0
* relocked
* added a zuul config, removed travis, CHANGELOG!!
* Automatic update of dependency thoth-common from 0.0.6 to 0.0.9
* Automatic update of dependency thoth-storages from 0.0.32 to 0.0.33
* Automatic update of dependency thoth-storages from 0.0.29 to 0.0.32
* rename ceph_host to s3_endpoint_url
* set resource limits of BC, DC; relocked Pipfile
* Automatic update of dependency thoth-storages from 0.0.28 to 0.0.29
* Automatic update of dependency thoth-storages from 0.0.25 to 0.0.28
* Automatic update of dependency thoth-common from 0.0.5 to 0.0.6
* Do not restrict Thoth packages
* Update thoth-common for rsyslog logging
* Add rsyslog logging
* Update thoth-storages
* Run coala in non-interactive mode
* Add missing coala dependencies
* Run Travis CI for now
* Update thoth-storages
* Use coala for code checks
* removed Travis-CI and 'docker build' stuff
* fixed a few typing glitches
* updated dependencies
* we need you!
* Fix slow ingestion - optimize syncs if the given document was already synced
* Update thoth-storages to respect schema
* Add license header
* Use proper LICENSE file
* Simplify CLI handling for s2i
* Enable pipenv on build
* Fix source strategy for BC
* Fix base image name
* Fix naming in openshift templates
* Fix template name
* Remove thoth- prefix
* Fix URL to repository
* Do not mix filenames
* Separate image stream
* Add cronjob template
* adding the OWNERS file
* Make analysis results host configurable
* Fix URL to repository and description
* Add README file
* need to put requirements.txt here by COPY and then RUN
* added an OpenShift BuildConfig and cleaned up the Dockerfile...
* Sync also analysis results to graph database
* Update thoth-storages
* Update thoth-storages to respect new result placing on Ceph
* Respect common logging configuration
* Update thoth-storages
* Connect adapters before use
* Solver result store has no longer envvar attribute
* Update thoth-storages package
* Do not die drastically on sync error
* Fix environment variable reference
* Update thoth-storages to respect API changes
* Graph database was renamed
* Update to use thoth storages
* Add graph syncing logic
* Add .travis.yml file
* Initial project import

## Release 0.6.2 (2020-06-01T14:10:54)
* :pushpin: Automatic update of dependency autopep8 from 1.5.2 to 1.5.3
* :pushpin: Automatic update of dependency thoth-common from 0.13.7 to 0.13.8
* :pushpin: Automatic update of dependency thoth-storages from 0.22.11 to 0.22.12
* :pushpin: Automatic update of dependency thoth-common from 0.13.6 to 0.13.7
* :pushpin: Automatic update of dependency prometheus-client from 0.7.1 to 0.8.0
* :pushpin: Automatic update of dependency thoth-common from 0.13.5 to 0.13.6
* :pushpin: Automatic update of dependency thoth-common from 0.13.4 to 0.13.5
* :pushpin: Automatic update of dependency thoth-storages from 0.22.10 to 0.22.11
* :pushpin: Automatic update of dependency thoth-common from 0.13.3 to 0.13.4

## Release 0.6.3 (2020-07-29T13:48:25)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.3 to 0.24.5 (#450)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.3 to 0.24.5 (#449)
* Remove latest versions limitation (#446)
* :pushpin: Automatic update of dependency thoth-common from 0.13.13 to 0.14.2 (#445)
* :pushpin: Automatic update of dependency thoth-common from 0.13.13 to 0.14.2 (#444)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.0 to 0.24.3 (#443)
* Fix trailing whitespace (#442)
* :pushpin: Automatic update of dependency sphinx-rtd-theme from 0.4.3 to 0.5.0 (#441)
* :pushpin: Automatic update of dependency sphinx-rtd-theme from 0.4.3 to 0.5.0 (#440)
* :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.13.13 (#439)
* :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.13.13 (#438)
* :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.24.0 (#437)
* Remove OpenShift templates as they are part of thoth-application (#436)
* Update OWNERS
* Remove registry related bits

## Release 0.7.0 (2020-07-30T09:57:33)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.5 to 0.25.0 (#457)
* :8ball: include ci config file and remove migrated files (#455)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.15.0 (#454)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.15.0 (#453)

## Release 0.7.1 (2020-07-30T10:24:29)
* :pushpin: Automatic update of dependency thoth-common from 0.15.0 to 0.16.0 (#461)
