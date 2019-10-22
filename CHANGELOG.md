# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.11.2]

### Changed

- Add option for setting `http2-max-field-size` via values.yaml.
- Add optional http snippet parameter to extend nginx http configuration.

## [0.11.1]

### Added

- Added a new configmap configuration to the chart for being able to add a [http snippet](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#http-snippet). 

## [0.11.0]

### Added

- Migrate chart into [nginx-ingress-controller-app](https://github.com/giantswarm/nginx-ingress-controller-app) repository as managed application. 

[kubernetes-nginx-ingress-controller](https://github.com/giantswarm/kubernetes-nginx-ingress-controller) repository is deprecated.

Previous versions changelog can be found [here](https://github.com/giantswarm/kubernetes-nginx-ingress-controller/blob/master/CHANGELOG.md)
