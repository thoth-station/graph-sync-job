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
