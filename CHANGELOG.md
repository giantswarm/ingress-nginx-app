# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

## [v1.6.9] 2020-04-22

### Changed

- Restrict PodSecurityPolicy volumes to only those required (removes wildcard).
- Tune `net.ipv4.ip_local_port_range` to `1024 65535` as a safe sysctl.
- Tune `net.core.somaxconn` to `32768` via an initContainer with privilege escalation.
- Use `4` worker processes by default.
- Use upstream default of max-worker-connections of `16384`.
- Ignore NGINX IC Deployment replica count configuration when HorizontalPodAutoscaler is enabled.
- Drop unnecessary Helm release revision annotation from NGINX IC Deployment.
- Adjust README for display in the web interface context.

## [v1.6.8] 2020-04-09

### Changed

- Default `max-worker-connections` to `0`, making it same as `max-worker-open-files` i.e. `max open files (system's limit) / worker-processes - 1024`.
  This optimizes for high load conditions where it improves performance at the cost of increasing RAM utilization (even on idle).
- HorizontalPodAutoscaler was tuned to use `targetMemoryUtilizationPercentage` of `80` due to increased RAM utilization with new default for `max-worker-connections` of `0`.
- Removed use of `enable-dynamic-certificates` CLI flag, it has been deprecated since [ingress-nginx 0.26.0](https://github.com/kubernetes/ingress-nginx/blob/master/Changelog.md#0260) via [ingress-nginx PR #4356](https://github.com/kubernetes/ingress-nginx/pull/4356)
- Changed default `error-log-level` from `error` to `notice`.
- Added a link to the README in the sources of Chart.yaml

## [v1.6.7] 2020-04-08

### Changed

- Align graceful termination configuration with changes made in upstream ingress-nginx 0.26.0 (see [related PR #4487](https://github.com/kubernetes/ingress-nginx/pull/4487#issuecomment-525588554) and important section in [0.26.0 release notes](https://github.com/kubernetes/ingress-nginx/releases/tag/nginx-0.26.0)).
  - Make NGINX IC Deployment's `terminationGracePeriodSeconds` configurable and align its default with `configmap.worker-shutdown-timeout`
  - Make NGINX IC controller container lifecycle hooks configurable, and change from `sleep 60` to using `/wait-shutdown` as preStop hook.
- Make `controller.minReadySeconds` configurable.

## [v1.6.6] 2020-04-01

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

[Unreleased]: https://github.com/giantswarm/nginx-ingress-controller-app/compare/v1.6.9...master
[v1.6.9]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.9
[v1.6.8]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.8
[v1.6.7]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.7
[v1.6.6]: https://github.com/giantswarm/nginx-ingress-controller-app/releases/tag/v1.6.6
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
