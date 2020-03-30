# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Change deployment to use release revision not time for Helm 3 support.

## [v1.6.5] 2020-03-23

### Changed

- Fix small cluster profile resource requests. ([#42](https://github.com/giantswarm/nginx-ingress-controller-app/pull/42))

## [v1.6.4] 2020-03-17

### Changed

- Disable HPA and PDB for xs clusters since NGINX Deployment resource requests are not set there. ([#40](https://github.com/giantswarm/nginx-ingress-controller-app/pull/40))

## [v1.6.3] 2020-03-16

### Changed

- Adjust resource requests, HPA and PDB depending on determined cluster profile; supported cluster profiles include xxs, xs, small, and larger than small or unknown. ([#38](https://github.com/giantswarm/nginx-ingress-controller-app/pull/38))

  By default, for nginx on:
  - xxs clusters - clear resource requests, HPA and PDB are disabled
  - xs clusters - clear resource requests, enabled HPA and PDB
  - small clusters - have some resource requests, HPA and PDB are enabled
  - clusters larger than small or unknown - have decent resource requests i.e. capacity out-of-the-box, and HPA and PDB are enabled.

## [v1.6.2] 2020-03-12

### Changed

- Reintroduced config properties which should have been just deprecated but got dropped prematurely in v1.4.0 ([#36](https://github.com/giantswarm/nginx-ingress-controller-app/pull/36))
  - `configmap.annotations-prefix`
  - `configmap.default-ssl-certificate`
  - `configmap.hpa-enabled`
  - `configmap.hpa-max-replicas`
  - `configmap.hpa-min-replicas`
  - `configmap.hpa-target-cpu-utilization-percentage`
  - `configmap.hpa-target-memory-utilization-percentage`
  - `configmap.ingress-class`

## [v1.6.1] 2020-03-10

### Changed

- Disable HPA, PDB and clear resource requests for extra small clusters. ([#34](https://github.com/giantswarm/nginx-ingress-controller-app/pull/34))

## [v1.6.0] 2020-02-28

### Changed

- Upgrade to nginx-ingress-controller 0.30.0. ([#31](https://github.com/giantswarm/nginx-ingress-controller-app/pull/31))
- Configured app icon. ([#32](https://github.com/giantswarm/nginx-ingress-controller-app/pull/32))
- Enabled HorizontalPodAutoscaler by default. ([#27](https://github.com/giantswarm/nginx-ingress-controller-app/pull/27))
- Based on HPA trials done so far, following settings have been adjusted to better fit actual observed usage profiles:
  - CPU resource requests have been adjusted from 500m to 2 CPU
    - 0.5 CPU was not enough for all the processes NGINX Ingress Controller starts
  - Memory requests changed from 600Mi to 2.5GB
    - Scaling out does not shard Ingress definitions and other configurations stored in memory of every nginx-ingress-controller replica
    - Memory usage spikes during configuration reloads
    - It improves the HPA stability
  - Default number of nginx worker processes was changed from 4 to 1
    - This reduced memory usage of each replica
    - It didn't affect request handling capacity
    - Better defaults considering CPU requests and number of processes running on every nginx-ingress-controller replica.
- To avoid cluster-operator and HPA collision and nginx service disruption, this release also breaks with cluster-operator controllable nginx ingress controller Deployment replicas count
  - `ingressController.replicas` which was previously dynamically set by cluster-operator is now removed
  - New `controller.replicaCount` config property is introduced, default replica count is set to 1, and then by default enabled HPA takes it over from there, by default scaling the Deployment in range of 1 to 20 replicas
  - If HPA gets disabled on-demand, replica count will stay static if not manually or automatically changed by some third party.

## [v1.5.0] 2020-02-18

### Changed

- Disable nginx NodePort Service by default, having legacy cluster-operator enable it for legacy Azure only. ([#29](https://github.com/giantswarm/nginx-ingress-controller-app/pull/29))
- Upgrade to nginx-ingress-controller 0.29.0. ([#30](https://github.com/giantswarm/nginx-ingress-controller-app/pull/30))

## [v1.4.0] 2020-02-10

### Changed

- Support overriding all nginx configmap settings. ([#26](https://github.com/giantswarm/nginx-ingress-controller-app/pull/26))

## [v1.3.0] 2020-01-30

### Changed

- Upgrade to nginx-ingress-controller 0.28.0. ([#24](https://github.com/giantswarm/nginx-ingress-controller-app/pull/24))

## [v1.2.1] 2020-01-29

### Changed

- Support proxy protocol for AWS. ([#23](https://github.com/giantswarm/nginx-ingress-controller-app/pull/23))

## [v1.2.0] 2020-01-21

### Changed

- Upgrade to nginx-ingress-controller 0.27.1. ([#20](https://github.com/giantswarm/nginx-ingress-controller-app/pull/20))
- Add metrics Service for prometheus-operator support. ([#19](https://github.com/giantswarm/nginx-ingress-controller-app/pull/19))
- Allow overriding of nginx SSL protocol default setting. ([#17](https://github.com/giantswarm/nginx-ingress-controller-app/pull/17))

## [v1.1.1] 2020-01-04

### Changed

- Updated manifests for Kubernetes 1.16. ([#16](https://github.com/giantswarm/nginx-ingress-controller-app/pull/16))

## [v1.1.0]

### Changed

- Migrate to managed application structure.

[kubernetes-nginx-ingress-controller](https://github.com/giantswarm/kubernetes-nginx-ingress-controller) repository is deprecated.

Previous versions changelog can be found [here](https://github.com/giantswarm/kubernetes-nginx-ingress-controller/blob/master/CHANGELOG.md)

[Unreleased]: https://github.com/giantswarm/nginx-ingress-controller-app/compare/v1.6.5...master
[v1.6.5]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.5
[v1.6.4]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.4
[v1.6.3]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.3
[v1.6.2]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.2
[v1.6.1]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.1
[v1.6.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.0
[v1.5.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.5.0
[v1.4.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.4.0
[v1.3.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.3.0
[v1.2.1]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.2.1
[v1.2.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.2.0
[v1.1.1]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.1.1
[v1.1.0]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.1.0
