# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Chart: Sync to upstream. ([#929](https://github.com/giantswarm/ingress-nginx-app/pull/929))
  - Controller: Update image to [v1.14.2](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.14.2.md).
  - Kube Webhook CertGen: Update image to v1.6.6.

## [4.2.1] - 2025-12-15

### Changed

- Chart: Sync to upstream. ([#916](https://github.com/giantswarm/ingress-nginx-app/pull/916))
  - Controller: Update image to [v1.14.1](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.14.1.md).
  - Kube Webhook CertGen: Update image to v1.6.5.

## [4.2.0] - 2025-11-05

### Added

- Chart: Sync to upstream. ([#903](https://github.com/giantswarm/ingress-nginx-app/pull/903))
  - Chart: Add volumes for webhook patch job.
  - Chart: Add resize policy.
  - Chart: `Add controller.metrics.serviceMonitor.scrapeTimeout`.

### Changed

- Chart: Sync to upstream. ([#903](https://github.com/giantswarm/ingress-nginx-app/pull/903))
  - Controller: Update image to [v1.14.0](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.14.0.md).
  - Kube Webhook CertGen: Update image to v1.6.4.
  - Chart: Make extra init containers templatable.

## [4.1.6] - 2026-01-27

### Changed

- Chart: Sync to upstream. ([#930](https://github.com/giantswarm/ingress-nginx-app/pull/930))
  - Controller: Update image to [v1.13.6](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.6.md).
  - Kube Webhook CertGen: Update image to v1.6.6.

## [4.1.5] - 2025-12-15

### Changed

- Chart: Sync to upstream. ([#917](https://github.com/giantswarm/ingress-nginx-app/pull/917))
  - Controller: Update image to [v1.13.5](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.5.md).
  - Kube Webhook CertGen: Update image to v1.6.5.

## [4.1.4] - 2025-11-04

### Changed

- Chart: Sync to upstream. ([#901](https://github.com/giantswarm/ingress-nginx-app/pull/901))
  - Controller: Update image to [v1.13.4](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.4.md).
  - Kube Webhook CertGen: Update image to v1.6.4.
  - Chart: Make `service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled` overridable.

## [4.1.3] - 2025-10-02

### Changed

- Chart: Sync to upstream. ([#881](https://github.com/giantswarm/ingress-nginx-app/pull/881))
  - Controller: Update image to [v1.13.3](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.3.md).
  - Kube Webhook CertGen: Update image to v1.6.3.

## [4.1.2] - 2025-08-29

### Changed

- Chart: Sync to upstream. ([#864](https://github.com/giantswarm/ingress-nginx-app/pull/864))
  - Controller: Update image to [v1.13.2](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.2.md).
  - Kube Webhook CertGen: Update image to v1.6.2.

## [4.1.1] - 2025-08-16

### Changed

- Chart: Sync to upstream. ([#849](https://github.com/giantswarm/ingress-nginx-app/pull/849))
  - Controller: Update image to [v1.13.1](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.1.md).
  - Kube Webhook CertGen: Update image to v1.6.1.

## [4.1.0] - 2025-07-18

### Added

- Chart: Sync to upstream. ([#833](https://github.com/giantswarm/ingress-nginx-app/pull/833))
  - Chart: Implement ServiceMonitor limits.
  - Chart: Add service cluster IPs.
  - Chart: Set `automountServiceAccountToken` in workloads.
  - Chart: Add `controller.service.trafficDistribution`.
  - Chart: Add `controller.service.external.labels` & `controller.service.internal.labels`.
  - Chart: Add `controller.admissionWebhooks.certManager.*.revisionHistoryLimit`.
  - Chart: Implement `runtimeClassName`.
  - Chart: Add `activeDeadlineSeconds`.

### Changed

- Updated E2E tests to use apptest-framework v1.14.0
- Chart: Sync to upstream. ([#833](https://github.com/giantswarm/ingress-nginx-app/pull/833))
  - Controller: Update image to [v1.13.0](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.13.0.md).

## [4.0.7] - 2025-11-04

### Added

- Chart: Sync to upstream. ([#899](https://github.com/giantswarm/ingress-nginx-app/pull/899))
  - Chart: Add `controller.service.trafficDistribution`.

### Changed

- Chart: Sync to upstream. ([#899](https://github.com/giantswarm/ingress-nginx-app/pull/899))
  - Controller: Update image to [v1.12.8](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.8.md).
  - Kube Webhook CertGen: Update image to v1.6.4.
  - Chart: Make `service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled` overridable.

## [4.0.6] - 2025-10-02

### Changed

- Chart: Sync to upstream. ([#878](https://github.com/giantswarm/ingress-nginx-app/pull/878))
  - Controller: Update image to [v1.12.7](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.7.md).
  - Kube Webhook CertGen: Update image to v1.6.3.

## [4.0.5] - 2025-08-29

### Changed

- Chart: Sync to upstream. ([#867](https://github.com/giantswarm/ingress-nginx-app/pull/867))
  - Controller: Update image to [v1.12.6](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.6.md).
  - Kube Webhook CertGen: Update image to v1.6.2.

## [4.0.4] - 2025-08-16

### Changed

- Chart: Sync to upstream. ([#848](https://github.com/giantswarm/ingress-nginx-app/pull/848))
  - Controller: Update image to [v1.12.5](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.5.md).
  - Kube Webhook CertGen: Update image to v1.6.1.

## [4.0.3] - 2025-07-17

### Changed

- Chart: Sync to upstream. ([#831](https://github.com/giantswarm/ingress-nginx-app/pull/831))
  - Controller: Update image to [v1.12.4](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.4.md).
  - Kube Webhook CertGen: Update image to v1.6.0.

## [4.0.2] - 2025-06-05

### Changed

- Chart: Sync to upstream. ([#815](https://github.com/giantswarm/ingress-nginx-app/pull/815))
  - Controller: Update image to [v1.12.3](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.3.md).
  - Kube Webhook CertGen: Update image to v1.5.4.

## [4.0.1] - 2025-05-01

### Changed

- Chart: Sync to upstream. ([#807](https://github.com/giantswarm/ingress-nginx-app/pull/807))
  - Controller: Update image to [v1.12.2](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.2.md).
  - Kube Webhook CertGen: Update image to v1.5.3.

## [4.0.0] - 2025-03-25

Depending on your current setup, this release may contain breaking changes. We go into these in more detail below and therefore ask you to read them carefully and check whether and to what extent they affect your setup.

### Added

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Deployment: Add `controller.progressDeadlineSeconds`.
  - Pod Disruption Budget: Add `controller.unhealthyPodEvictionPolicy`.
  - Prometheus Rule: Add `controller.metrics.prometheusRule.annotations`.
  - Metrics Service: Add `controller.metrics.service.enabled`.
  - Default Backend: Add `defaultBackend.maxUnavailable`.
  - Default Backend: Add `defaultBackend.unhealthyPodEvictionPolicy`.

### Changed

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Controller: Update image to [v1.12.0](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.0.md).\
    **NOTE:** Please read the upstream changelog carefully, especially the entries marked with ⚠️. In addition, the following should be noted:
    - The `--enable-annotation-validation` CLI flag is already enabled by default in this app since v3.2.0.
    - The `allow-cross-namespace-resources` ConfigMap option getting deactivated affects you if you are currently referencing resources such as Secrets in Ingress resource annotations from namespaces other than the Ingress resource itself.
    - The `annotations-risk-level` ConfigMap option getting lowered to `High` affects you if you are currently using annotations with an annotation risk level of `Critical`. Especially snippet annotations belong to this annotation risk level. So even though you activated snippet annotations via ConfigMap option in the past, you now also need to increase the `annotations-risk-level` ConfigMap option back to `Critical`.
    - The `strict-validate-path-type` ConfigMap option is already enabled by default in this app since v3.2.0.
  - Values: Rename `image` to `global.image`.
- Chart: Sync to upstream. ([#788](https://github.com/giantswarm/ingress-nginx-app/pull/788))
  - Controller: Update image to [v1.12.1](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.1.md).
  - Kube Webhook CertGen: Update image to v1.5.2.

### Removed

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Chart: Remove Pod Security Policies.\
    **NOTE:** Pod Security Policies have already been removed from Kubernetes in v1.25. Therefore, this version is not compatible with Kubernetes v1.24 and below.
  - Values: Remove `configmap`.\
    **NOTE:** The `configmap` value is deprecated since v3.0.0. Please use `controller.config` instead.
  - Deployment: Remove `giantswarm.io/monitoring_basic_sli` label.
  - Deployment: Remove OpenTelemetry init container.\
    **NOTE:** OpenTelemetry is still supported, but since the module is built into the controller image since v1.10, we hereby remove the init container and image which were used to install it upon controller startup.

## [4.0.0-alpha1] - 2025-01-30

Depending on your current setup, this release may contain breaking changes. We go into these in more detail below and therefore ask you to read them carefully and check whether and to what extent they affect your setup.

### Added

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Deployment: Add `controller.progressDeadlineSeconds`.
  - Pod Disruption Budget: Add `controller.unhealthyPodEvictionPolicy`.
  - Prometheus Rule: Add `controller.metrics.prometheusRule.annotations`.
  - Metrics Service: Add `controller.metrics.service.enabled`.
  - Default Backend: Add `defaultBackend.maxUnavailable`.
  - Default Backend: Add `defaultBackend.unhealthyPodEvictionPolicy`.

### Changed

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Controller: Update image to [v1.12.0](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.12.0.md).\
    **NOTE:** Please read the upstream changelog carefully, especially the entries marked with ⚠️. In addition, the following should be noted:
    - The `--enable-annotation-validation` CLI flag is already enabled by default in this app since v3.2.0.
    - The `allow-cross-namespace-resources` ConfigMap option getting deactivated affects you if you are currently referencing resources such as Secrets in Ingress resource annotations from namespaces other than the Ingress resource itself.
    - The `annotations-risk-level` ConfigMap option getting lowered to `High` affects you if you are currently using annotations with an annotation risk level of `Critical`. Especially snippet annotations belong to this annotation risk level. So even though you activated snippet annotations via ConfigMap option in the past, you now also need to increase the `annotations-risk-level` ConfigMap option back to `Critical`.
    - The `strict-validate-path-type` ConfigMap option is already enabled by default in this app since v3.2.0.
  - Values: Rename `image` to `global.image`.

### Removed

- Chart: Sync to upstream. ([#768]()https://github.com/giantswarm/ingress-nginx-app/pull/768)
  - Chart: Remove Pod Security Policies.\
    **NOTE:** Pod Security Policies have already been removed from Kubernetes in v1.25. Therefore, this version is not compatible with Kubernetes v1.24 and below.
  - Values: Remove `configmap`.\
    **NOTE:** The `configmap` value is deprecated since v3.0.0. Please use `controller.config` instead.
  - Deployment: Remove `giantswarm.io/monitoring_basic_sli` label.
  - Deployment: Remove OpenTelemetry init container.\
    **NOTE:** OpenTelemetry is still supported, but since the module is built into the controller image since v1.10, we hereby remove the init container and image which were used to install it upon controller startup.

## [3.9.8] - 2025-07-17

### Changed

- Chart: Sync to upstream. ([#829](https://github.com/giantswarm/ingress-nginx-app/pull/829))
  - Controller: Update image to [v1.11.8](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.8.md).
  - Kube Webhook CertGen: Update image to v1.6.0.

## [3.9.7] - 2025-06-05

### Changed

- Chart: Sync to upstream. ([#813](https://github.com/giantswarm/ingress-nginx-app/pull/813))
  - Controller: Update image to [v1.11.7](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.7.md).
  - Kube Webhook CertGen: Update image to v1.5.4.

## [3.9.6] - 2025-05-01

### Changed

- Chart: Sync to upstream. ([#805](https://github.com/giantswarm/ingress-nginx-app/pull/805))
  - Controller: Update image to [v1.11.6](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.6.md).
  - Kube Webhook CertGen: Update image to v1.5.3.

## [3.9.5] - 2025-03-25

### Changed

- Chart: Sync to upstream. ([#789](https://github.com/giantswarm/ingress-nginx-app/pull/789))
  - Controller: Update image to [v1.11.5](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.5.md).
  - Kube Webhook CertGen: Update image to v1.5.2.

## [3.9.4] - 2025-01-06

### Changed

- Chart: Sync to upstream. ([#760](https://github.com/giantswarm/ingress-nginx-app/pull/760))
  - Controller: Update image to [v1.11.4](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.4.md).
  - Kube Webhook CertGen: Update image to v1.5.0.

## [3.9.3] - 2024-11-06

### Changed

- Chart: Sync to upstream. ([#741](https://github.com/giantswarm/ingress-nginx-app/pull/741))
  - Controller: Update image to [v1.11.3](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.3.md).
  - Kube Webhook CertGen: Update image to v1.4.4.
  - Chart: Implement `controller.admissionWebhooks.service.servicePort`.
  - Chart: Rework ServiceMonitor.
  - Chart: Align default backend `PodDisruptionBudget`.
  - Chart: Specify `matchLabelKeys` in Topology Spread Constraints.

## [3.9.2] - 2024-08-20

### Changed

- Chart: Sync to upstream. ([#687](https://github.com/giantswarm/ingress-nginx-app/pull/687))
  - Controller: Update image to [v1.11.2](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.2.md).
  - OpenTelemetry: Update image to v20240813-b933310d.
  - Kube Webhook CertGen: Update image to v1.4.3.

### Removed

- Chart: Sync to upstream. ([#687](https://github.com/giantswarm/ingress-nginx-app/pull/687))
  - Helpers: Remove useless `isControllerTagValid`.

## [3.9.1] - 2024-07-29

### Added

- Chart: Sync to upstream. ([#687](https://github.com/giantswarm/ingress-nginx-app/pull/687))
  - Chart: Explicitly set `runAsGroup`.

## [3.9.0] - 2024-07-21

### Added

- Chart: Sync to upstream. ([#673](https://github.com/giantswarm/ingress-nginx-app/pull/673))
  - Values: Add `controller.disableLeaderElection`.
  - Values: Add `controller.electionTTL`.

### Changed

- Chart: Sync to upstream. ([#673](https://github.com/giantswarm/ingress-nginx-app/pull/673))
  - Controller: Update image to [`v1.11.1`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.11.1.md).

## [3.8.1] - 2024-07-21

### Changed

- Controller: Update image to [`v1.10.3`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.10.3.md). ([#671](https://github.com/giantswarm/ingress-nginx-app/pull/671))

## [3.8.0] - 2024-06-18

### Changed

- Deployments/DaemonSets: Make pod affinity templatable. ([#654](https://github.com/giantswarm/ingress-nginx-app/pull/654))
- ServiceMonitor: Relabel app & node. ([#654](https://github.com/giantswarm/ingress-nginx-app/pull/654))

## [3.7.0] - 2024-06-03

### Added

- Ingress Class: Make annotations configurable. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Admission Webhook: Make patch job RBAC configurable. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Default Backend: Add topology spread constraints. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))

### Changed

- Chart: Require Kubernetes version >= 1.21.0-0. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Config Map: Support templates in values. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Service: Fix app protocol semver comparison. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Admission Webhook: Update patch job image to `v1.4.1`. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))
- Default Backend: Reorder HPA. ([#639](https://github.com/giantswarm/ingress-nginx-app/pull/639))

## [3.6.1] - 2024-06-03

### Changed

- Controller: Update image to [`v1.10.1`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.10.1.md). ([#640](https://github.com/giantswarm/ingress-nginx-app/pull/640))

## [3.6.0] - 2024-03-26

Since upstream did not release a `chroot` variant of the controller image for v1.10.0, one can not enable `controller.image.chroot` in the chart values. If you although try to do so, your pods will not come up due to a missing image.

We are sorry for that inconvenience and hopefully bring back support for that in a future version!

### Added

- Chart: Add IngressClass aliases. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))

### Changed

- Image: Update to [`v1.10.0`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.10.0.md). ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))\
  **NOTE:** Upstream does not provide a `chroot` image for this version, yet.
- Chart: Always deploy `PrometheusRule` when asked to. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))
- Chart: Deploy `PodDisruptionBudget` with KEDA. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))
- Chart: Improve IngressClass documentation. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))
- Chart: Align HPA & KEDA conditions. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))
- Chart: Render `controller.ingressClassResource.parameters` natively. ([#609](https://github.com/giantswarm/ingress-nginx-app/pull/609))

## [3.5.2] - 2024-02-23

### Changed

- Metrics: Really disable them when told to. ([#592](https://github.com/giantswarm/ingress-nginx-app/pull/592))

## [3.5.1] - 2024-01-27

### Changed

- Image: Update to [`v1.9.6`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.9.6.md). ([#584](https://github.com/giantswarm/ingress-nginx-app/pull/584))

## [3.5.0] - 2024-01-15

### Added

- Service: Add CAPZ support. ([#587](https://github.com/giantswarm/ingress-nginx-app/pull/587))

## [3.4.2] - 2023-12-21

### Added

- Service Monitor: Add `controller.metrics.serviceMonitor.annotations`. ([#584](https://github.com/giantswarm/ingress-nginx-app/pull/584))

### Changed

- Image: Update to [`v1.9.5`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/controller-1.9.5.md). ([#584](https://github.com/giantswarm/ingress-nginx-app/pull/584))
- Default Backend: Label pods with `ingress-nginx.labels` instead of `ingress-nginx.selectorLabels`. ([#584](https://github.com/giantswarm/ingress-nginx-app/pull/584))

## [3.4.1] - 2023-12-15

### Added

- Chart: Add Helm unit tests from upstream. ([#578](https://github.com/giantswarm/ingress-nginx-app/pull/578))

### Changed

- Role: Omit Ingress status permissions if `--update-chart=false`. ([#579](https://github.com/giantswarm/ingress-nginx-app/pull/579))

## [3.4.0] - 2023-12-13

### Added

- Service: Add `controller.service.internal.type`. ([#571](https://github.com/giantswarm/ingress-nginx-app/pull/571))
- Default Backend: Add `defaultBackend.extraConfigMaps`. ([#576](https://github.com/giantswarm/ingress-nginx-app/pull/576))

### Changed

- Chart: Simplify image templating. ([#571](https://github.com/giantswarm/ingress-nginx-app/pull/571))
- Deployment: Make extra modules image more configurable. ([#572](https://github.com/giantswarm/ingress-nginx-app/pull/572))\
  **NOTE:** This changes the schema of `controller.extraModules.image` & `controller.opentelemetry.image`. Please update any overrides.
- Configure `gsoci.azurecr.io` as the default container image registry. ([#574](https://github.com/giantswarm/ingress-nginx-app/pull/574))

## [3.3.1] - 2023-12-05

### Added

- Admission Webhook: Add `controller.admissionWebhooks.patch.networkPolicy.enabled`. ([#568](https://github.com/giantswarm/ingress-nginx-app/pull/568))

## [3.3.0] - 2023-11-21

### Added

- Chart: Add `namespaceOverride`. ([#565](https://github.com/giantswarm/ingress-nginx-app/pull/565))
- Service: Add `controller.service.allocateLoadBalancerNodePorts` & `controller.service.internal.allocateLoadBalancerNodePorts`. ([#565](https://github.com/giantswarm/ingress-nginx-app/pull/565))

### Changed

- Admission Webhook: Truncate name. ([#565](https://github.com/giantswarm/ingress-nginx-app/pull/565))

## [3.2.1] - 2023-10-26

### Changed

- Image: Update to [`v1.9.4`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.9.4.md). ([#557](https://github.com/giantswarm/ingress-nginx-app/pull/557))

## [3.2.0] - 2023-10-18

This release contains security relevant changes. Please check your `Ingress` resources for invalid annotations or paths before installing it.

### Changed

- Values: Enable `controller.enableAnnotationValidations` by default. ([#552](https://github.com/giantswarm/ingress-nginx-app/pull/552))\
  **NOTE:** This change affects existing, new & updated `Ingress` resources. Upstream is enabling this by default, too: https://github.com/kubernetes/ingress-nginx/issues/10186.
- Values: Enable `controller.config.strict-validate-path-type` by default. ([#553](https://github.com/giantswarm/ingress-nginx-app/pull/553))\
  **NOTE:** This change affects new & updated `Ingress` resources only. Upstream is enabling this by default, too: https://github.com/kubernetes/ingress-nginx/issues/10186.\
  See https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#strict-validate-path-type for further information.

## [3.1.2] - 2023-10-26

### Changed

- Image: Update to [`v1.9.4`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.9.4.md). ([#557](https://github.com/giantswarm/ingress-nginx-app/pull/557))

## [3.1.1] - 2023-10-18

### Changed

- Controller: Fix `chroot` mode. ([#550](https://github.com/giantswarm/ingress-nginx-app/pull/550))

### Removed

- Service: Remove redundant version check. ([#550](https://github.com/giantswarm/ingress-nginx-app/pull/550))

## [3.1.0] - 2023-10-12

### Added

- Controller: Add `controller.enableAnnotationValidations`. ([#536](https://github.com/giantswarm/ingress-nginx-app/pull/536))
- OpenTelemetry: Add `controller.opentelemetry.resources`. ([#536](https://github.com/giantswarm/ingress-nginx-app/pull/536))
- Values: Add `global.podSecurityStandards.enforced`. ([#544](https://github.com/giantswarm/ingress-nginx-app/pull/544))

### Changed

- Image: Update to [`v1.9.0`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.9.0.md). ([#536](https://github.com/giantswarm/ingress-nginx-app/pull/536))
- Deployment/DaemonSet: Make `controller.topologySpreadConstraints` an array. ([#536](https://github.com/giantswarm/ingress-nginx-app/pull/536))\
  **NOTE:** This is part of our alignment to upstream. Please convert any overrides of `controller.topologySpreadConstraints` to an array, too.
- Tests: Upgrade dependencies & remove explicit ATS version. ([#538](https://github.com/giantswarm/ingress-nginx-app/pull/538))
- Service: Fix wildcard subdomain. ([#539](https://github.com/giantswarm/ingress-nginx-app/pull/539))
- Chart: Tighten `securityContext`s and Pod Security Policies. ([#540](https://github.com/giantswarm/ingress-nginx-app/pull/540))
- OpenTelemetry: Use own registry. ([#541](https://github.com/giantswarm/ingress-nginx-app/pull/541))
- Admission Webhooks: Update `kube-webhook-certgen` image to `v20231011-8b53cabe0`. ([#542](https://github.com/giantswarm/ingress-nginx-app/pull/542))
- Image: Update to [`v1.9.3`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.9.3.md). ([#547](https://github.com/giantswarm/ingress-nginx-app/pull/547))

### Removed

- Controller: Drop support for `controller.kind: Both`. ([#547](https://github.com/giantswarm/ingress-nginx-app/pull/547))

## [3.0.2] - 2023-10-12

### Changed

- Image: Update to [`v1.8.4`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.8.4.md). ([#545](https://github.com/giantswarm/ingress-nginx-app/pull/545))
- Tests: Upgrade dependencies & remove explicit ATS version. ([#538](https://github.com/giantswarm/ingress-nginx-app/pull/538))

## [3.0.1] - 2023-09-18

### Changed

- Service Account: Align annotation format. ([#526](https://github.com/giantswarm/ingress-nginx-app/pull/526))
- Image: Update to [`v1.8.2`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.8.2.md). ([#532](https://github.com/giantswarm/ingress-nginx-app/pull/532))

## [3.0.0] - 2023-08-28

This is the first public stable release of our new `ingress-nginx` chart.

If you are currently using `v2.x.x`, this release includes breaking changes. We set up a [migration guide](https://github.com/giantswarm/ingress-nginx-app/blob/v3.0.0/migration.md) to make the upgrade as smooth as possible. Notable changes requiring your attention and/or manual intervention, like renaming, deprecation or removal of values, have been highlighted below.

Even though we highly recommend to upgrade to this and future releases, `v2.x.x` will continue to receive bugfixes as long as possible.

All feedback regarding this release, its changes, or our [migration guide](https://github.com/giantswarm/ingress-nginx-app/blob/v3.0.0/migration.md) is very welcome!

### Added

- Service: Align features from external service to internal one. ([#467](https://github.com/giantswarm/ingress-nginx-app/pull/467))
- Service: Add `controller.service.internal.ports` & `controller.service.internal.targetPorts`. ([#469](https://github.com/giantswarm/ingress-nginx-app/pull/469))
- PDB: Add `controller.annotations`. ([#481](https://github.com/giantswarm/ingress-nginx-app/pull/481))
- KEDA: Add `fallback`. ([#497](https://github.com/giantswarm/ingress-nginx-app/pull/497))
- OpenTelemetry: Add distroless `init_module`. ([#498](https://github.com/giantswarm/ingress-nginx-app/pull/498))
- Service: Add `controller.service.loadBalancerClass`. ([#503](https://github.com/giantswarm/ingress-nginx-app/pull/503))\
  **NOTE:** The load balancer class of existing services can not be changed. The app deployment might fail when defining this for already installed app instances.
- Deployment: Ignore `replicaCount` with KEDA enabled. ([#513](https://github.com/giantswarm/ingress-nginx-app/pull/513))
- Service: Template annotations. ([#514](https://github.com/giantswarm/ingress-nginx-app/pull/514))
- Deployment/DaemonSet: Add `controller.hostAliases`. ([#521](https://github.com/giantswarm/ingress-nginx-app/pull/521))

### Changed

- Helpers: Align labels to upstream. ([#450](https://github.com/giantswarm/ingress-nginx-app/pull/450))
- Values: Align CPU & memory requests to actual needs. ([#453](https://github.com/giantswarm/ingress-nginx-app/pull/453))\
  **NOTE:** This reduces the default resource requests. Please review & configure them to your actual needs.
- Values: Deprecate `configmap`, use `controller.config` instead. ([#463](https://github.com/giantswarm/ingress-nginx-app/pull/463))\
  **NOTE:** This is part of our alignment to upstream. Use `controller.config` instead.
- Chart: Rename to `ingress-nginx`. ([#464](https://github.com/giantswarm/ingress-nginx-app/pull/464))
- HPA: Align to upstream. ([#465](https://github.com/giantswarm/ingress-nginx-app/pull/465))
- PDB: Improve checks. ([#487](https://github.com/giantswarm/ingress-nginx-app/pull/487))
- Images: Update OpenTelemetry & kube-webhook-certgen image. ([#488](https://github.com/giantswarm/ingress-nginx-app/pull/488))
- Image: Update to [`v1.8.0`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.8.0.md). ([#489](https://github.com/giantswarm/ingress-nginx-app/pull/489))
- HPA: Partially revert [#465](https://github.com/giantswarm/ingress-nginx-app/pull/465). ([#493](https://github.com/giantswarm/ingress-nginx-app/pull/493))
- Metrics: Use `ServiceMonitor`. ([#494](https://github.com/giantswarm/ingress-nginx-app/pull/494))
- Image: Update to [`v1.8.1`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.8.1.md). ([#505](https://github.com/giantswarm/ingress-nginx-app/pull/505))
- Values: Update docs about `controller.enableTopologyAwareRouting`. ([#520](https://github.com/giantswarm/ingress-nginx-app/pull/520))
- OpenTelemetry: Update image to `v20230721-3e2062ee5`. ([#522](https://github.com/giantswarm/ingress-nginx-app/pull/522))
- ServiceMonitor: Explicitly set namespace. ([#523](https://github.com/giantswarm/ingress-nginx-app/pull/523))

### Removed

- Service: Remove `controller.service.suffix` & `controller.service.internal.suffix`. ([#448](https://github.com/giantswarm/ingress-nginx-app/pull/448))\
  **NOTE:** This is part of our alignment to upstream. There is no replacement for this key.
- Params: Align to upstream. ([#452](https://github.com/giantswarm/ingress-nginx-app/pull/452))
  - Params: Remove `controller.annotationsPrefix`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.extraArgs` instead.
  - Params: Remove `controller.defaultSSLCertificate`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.extraArgs` instead.
  - Params: Remove `controller.enableSSLChainCompletion`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.extraArgs` instead.
  - Params: Remove `controller.updateIngressStatus`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.extraArgs` instead.
- Service: Remove default values for `controller.service.nodePorts` & `controller.service.internal.nodePorts`. ([#461](https://github.com/giantswarm/ingress-nginx-app/pull/461))\
  **NOTE:** If you are running on our KVM product, please make sure to manually set those keys to their prior values.
- Params: Remove `controller.disableExternalNameForwarding`. ([#462](https://github.com/giantswarm/ingress-nginx-app/pull/462))\
  **NOTE:** This is part of our alignment to upstream. Use `controller.extraArgs` instead.

## [2.30.1] - 2023-05-07

### Changed

- Image: Update to [`v1.7.1`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.7.1.md). ([#473](https://github.com/giantswarm/ingress-nginx-app/pull/473))

## [2.30.0] - 2023-04-18

Since we started working on aligning this chart to upstream as much as possible a while ago, this might be the last non-breaking release.

We're currently working on releasing v3.0.0, including several breaking changes and requiring to re-install the chart.

### Removed

- Deployment/DaemonSet: Remove `cluster-autoscaler.kubernetes.io/safe-to-evict` annotation. ([#449](https://github.com/giantswarm/ingress-nginx-app/pull/449))
- Deployment/DaemonSet: Remove duplicate Prometheus annotations. ([#455](https://github.com/giantswarm/ingress-nginx-app/pull/455))
- Values: Remove `configmap` keys matching defaults. ([#457](https://github.com/giantswarm/ingress-nginx-app/pull/457))
  - Values: Remove `configmap.error-log-level`.
  - Values: Remove `configmap.server-name-hash-bucket-size`.
  - Values: Remove `configmap.worker-processes`.
  - Values: Remove `configmap.worker-shutdown-timeout`.
  - Values: Remove `configmap.use-forwarded-headers`.
- Service: Remove deprecated & default annotations. ([#458](https://github.com/giantswarm/ingress-nginx-app/pull/458))

## [2.29.0] - 2023-04-03

### Added

- Default Backend: Add `NetworkPolicy`. ([#443](https://github.com/giantswarm/ingress-nginx-app/pull/443))

### Changed

- DaemonSet: Align to `Deployment` (and vice versa). ([#442](https://github.com/giantswarm/ingress-nginx-app/pull/442))

## [2.28.0] - 2023-04-01

### Added

- Service: Add vCloud AVI annotations. ([#439](https://github.com/giantswarm/ingress-nginx-app/pull/439))

### Changed

- Image: Update to [`v1.7.0`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.7.0.md). ([#440](https://github.com/giantswarm/ingress-nginx-app/pull/440))

## [2.27.0] - 2023-03-22

### Added

- Helpers: Align to upstream. ([#429](https://github.com/giantswarm/ingress-nginx-app/pull/429))
  - Helpers: Add `controller.containerSecurityContext`.
  - Helpers: Add `ingress-nginx.image`.
  - Helpers: Add `ingress-nginx.imageDigest`.
  - Helpers: Add `ingress-nginx.controller.publishServicePath`.
  - Helpers: Add `ingress-nginx.params`.
  - Helpers: Add `isControllerTagValid`.
  - Helpers: Add `extraModules`.
- Chart: Align to upstream. ([#431](https://github.com/giantswarm/ingress-nginx-app/pull/431))
  - Chart: Add `.helmignore`.
  - Chart: Add `NOTES.txt`.
- Chart: Add CI values from upstream. ([#432](https://github.com/giantswarm/ingress-nginx-app/pull/432))
- Deployment: Align to upstream. ([#433](https://github.com/giantswarm/ingress-nginx-app/pull/433))
  - Deployment: Implement `controller.kind`.
  - Deployment: Implement `controller.labels`.
  - Deployment: Implement `controller.annotations`.
  - Deployment: Implement `revisionHistoryLimit`.
  - Deployment: Implement `controller.podAnnotations`.
  - Deployment: Implement `controller.dnsConfig`.
  - Deployment: Implement `controller.hostname`.
  - Deployment: Implement `controller.dnsPolicy`.
  - Deployment: Implement `controller.podLabels`.
  - Deployment: Implement `imagePullSecrets`.
  - Deployment: Implement `controller.priorityClassName`.\
    **NOTE**: Removes the hardcoded default `system-cluster-critical`. Please override if required.
  - Deployment: Implement `controller.podSecurityContext` & `controller.sysctls`.
  - Deployment: Implement `controller.shareProcessNamespace`.
  - Deployment: Implement `controller.containerName`.
  - Deployment: Implement `controller.updateStrategy`.
  - Deployment: Implement `controller.publishService`.
  - Deployment: Implement `controller.ingressClass`.\
    **NOTE**: If you are currently overriding `controller.ingressClassResource.name`, there are two cases which require manual intervention:

    * You are assigning ingresses to an ingress controller by annotation.
    * You enabled `controller.ingressClassByName`.

    Please set `controller.ingressClass` to the value of `controller.ingressClassResource.name` if any of these cases applies to you.
  - Deployment: Implement `controller.configMapNamespace`.
  - Deployment: Implement `controller.tcp.configMapNamespace`.
  - Deployment: Implement `controller.udp.configMapNamespace`.
  - Deployment: Implement `controller.scope.namespace`.
  - Deployment: Implement `controller.scope.namespaceSelector`.
  - Deployment: Implement `controller.reportNodeInternalIp`.
  - Deployment: Implement `controller.admissionWebhooks.certificate` & `controller.admissionWebhooks.key`.
  - Deployment: Implement `controller.maxmindLicenseKey`.
  - Deployment: Implement `controller.healthCheckHost`.
  - Deployment: Implement `controller.healthCheckPath`.
  - Deployment: Implement `controller.enableTopologyAwareRouting`.
  - Deployment: Implement `controller.extraArgs`.
  - Deployment: Implement `serviceAccount.name`.
  - Deployment: Implement `controller.containerSecurityContext`.
  - Deployment: Implement `controller.hostPort`.
  - Deployment: Implement `controller.metrics.portName`.
  - Deployment: Implement `tcp` & `udp` ports.
  - Deployment: Implement `controller.customTemplate`.
  - Deployment: Implement `controller.extraVolumeMounts`.
  - Deployment: Implement `controller.opentelemetry`.
  - Deployment: Implement `controller.extraContainers`.
  - Deployment: Implement `controller.extraInitContainers`.
  - Deployment: Implement `controller.hostNetwork`.
  - Deployment: Implement `controller.nodeSelector`.
  - Deployment: Implement `controller.tolerations`.
  - Deployment: Implement `controller.affinity`.
  - Deployment: Add `DaemonSet` option.

### Changed

- Helpers: Align to upstream. ([#429](https://github.com/giantswarm/ingress-nginx-app/pull/429))
  - Helpers: Rename `name` to `ingress-nginx.name`.
  - Helpers: Rename `chart` to `ingress-nginx.chart`.
  - Helpers: Align `ingress-nginx.fullname`.
  - Helpers: Align `ingress-nginx.controller.fullname`.
  - Helpers: Align `ingress-nginx.controller.electionID`.
  - Helpers: Align `ingress-nginx.defaultBackend.fullname`.
  - Helpers: Align `ingress-nginx.labels`.
  - Helpers: Align `ingress-nginx.selectorLabels`.
  - Helpers: Align `ingress-nginx.defaultBackend.serviceAccountName`.
- Chart: Align to upstream. ([#431](https://github.com/giantswarm/ingress-nginx-app/pull/431))
  - Chart: Align `Chart.yaml`.
- HPA: Use capabilities, reorder `if`. ([#434](https://github.com/giantswarm/ingress-nginx-app/pull/434))
- Deployment: Align to upstream. ([#433](https://github.com/giantswarm/ingress-nginx-app/pull/433))
  - Deployment: Align `controller.image`.
  - Deployment: Align `startupProbe`.\
    **NOTE**: Please remove `controller.startupProbe.enabled` from your overrides and remove/set `controller.startupProbe` instead.
  - Deployment: Align `livenessProbe`.\
    **NOTE**: Please remove `controller.livenessProbe.enabled` from your overrides and remove/set `controller.livenessProbe` instead.
  - Deployment: Align `readinessProbe`.\
    **NOTE**: Please remove `controller.readinessProbe.enabled` from your overrides and remove/set `controller.readinessProbe` instead.
  - Deployment: Update `controller.image.tag` to [`v1.6.4`](https://github.com/kubernetes/ingress-nginx/blob/main/changelog/Changelog-1.6.4.md).

### Removed

- Helpers: Align to upstream. ([#429](https://github.com/giantswarm/ingress-nginx-app/pull/429))
  - Helpers: Remove `resource.controller-service-internal.name`.
  - Helpers: Remove `resource.controller-service.name`.
- Deployment: Align to upstream. ([#433](https://github.com/giantswarm/ingress-nginx-app/pull/433))
  - Deployment: Remove `controller.extraAnnotations.deployment`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.annotations` instead.
  - Deployment: Remove `controller.extraAnnotations.pod`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.podAnnotations` instead.
  - Deployment: Remove `sysctls` setting `net.ipv4.ip_local_port_range`.\
    **NOTE:** Set via `controller.sysctls` if required.
  - Deployment: Remove `initContainers` setting `net.core.somaxconn`.\
    **NOTE:** Set via `controller.sysctls` if required.
  - Deployment: Remove `controller.maxSurge`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.updateStrategy` instead.
  - Deployment: Remove `controller.maxUnavailable`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.updateStrategy` instead.
  - Deployment: Remove `controller.userID`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.image.runAsUser` instead.
  - Deployment: Remove `controller.groupID`.\
    **NOTE:** This is part of our alignment to upstream. There is no replacement for this key.
  - Deployment: Remove `controller.antiAffinityScheduling` & `controller.nodeAffinity`.
    **NOTE:** This is part of our alignment to upstream. Use `controller.affinity` instead.

## [2.26.0] - 2023-03-09

### Added

- Service: Align to upstream. ([#425](https://github.com/giantswarm/ingress-nginx-app/pull/425))
  - Service: Implement `controller.service.clusterIP`.\
    **NOTE:** The cluster IP of existing services can not be changed. The app deployment might fail when defining this for already installed app instances.
  - Service: Implement `controller.service.externalIPs`.
  - Service: Implement `controller.service.loadBalancerIP`.
  - Service: Implement `controller.service.sessionAffinity`.
  - Service: Implement `controller.service.healthCheckNodePort`.\
    **NOTE:** The health check node port of existing services can not be changed. The app deployment might fail when defining this for already installed app instances.
  - Service: Implement `controller.service.ipFamilyPolicy`.
  - Service: Implement `controller.service.ipFamilies`.
  - Service: Implement `controller.service.enableHttp`.
  - Service: Implement `controller.service.enableHttps`.
  - Service: Implement `controller.service.appProtocol`.
  - Service: Implement `controller.service.external.enabled`.
  - Service: Add `portNamePrefix`.
  - Service: Add `controller.service.nodePorts.tcp` & `controller.service.nodePorts.udp`.
  - Service: Implement node ports for `tcp` and `udp`.
  - Internal Service: Implement `controller.service.internal.loadBalancerIP`.
  - Internal Service: Implement `controller.service.enableHttp` & `controller.service.enableHttps`.
  - Internal Service: Implement `controller.service.appProtocol`.
  - Internal Service: Add `controller.service.internal.nodePorts.tcp` & `controller.service.internal.nodePorts.udp`.
  - Internal Service: Implement node ports for `tcp` and `udp`.

### Changed

- Service: Align to upstream. ([#425](https://github.com/giantswarm/ingress-nginx-app/pull/425))
  - Service: Reorder name & namespace.
  - Service: Align `controller.service.loadBalancerSourceRanges`.
  - Service: Align `controller.service.externalTrafficPolicy`.
  - Service: Align indention of `ports`.
  - Service: Align node port checks.
  - Internal Service: Align initial check.
  - Internal Service: Reorder name & namespace.
  - Internal Service: Align `controller.service.internal.loadBalancerSourceRanges`.
  - Internal Service: Reorder `controller.service.internal.externalTrafficPolicy`.
  - Internal Service: Align indention of `ports`.
  - Internal Service: Align node port checks.
  - Values: Align to upstream.

### Removed

- Service: Align to upstream. ([#425](https://github.com/giantswarm/ingress-nginx-app/pull/425))
  - Internal Service: Remove `controller.service.internal.labels`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.service.labels` instead.
  - Internal Service: Remove `controller.service.internal.type`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.service.type` instead.
  - Internal Service: Remove `controller.service.internal.ports.http`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.service.ports.http` instead.
  - Internal Service: Remove `controller.service.internal.ports.https`.\
    **NOTE:** This is part of our alignment to upstream. Use `controller.service.ports.https` instead.

## [2.25.1] - 2023-03-03

### Fixed

- Webhook: Remove digest from image. ([#426](https://github.com/giantswarm/ingress-nginx-app/pull/426))

## [2.25.0] - 2023-03-02

### Added

- Default Backend: Add `defaultBackend.updateStrategy` & `defaultBackend.minReadySeconds`. ([#406](https://github.com/giantswarm/ingress-nginx-app/pull/406))
- ConfigMap: Align to upstream. ([#409](https://github.com/giantswarm/ingress-nginx-app/pull/409))
  - ConfigMap: Implement `controller.configAnnotations`.
  - ConfigMap: Implement `controller.addHeaders`.
  - ConfigMap: Implement `controller.proxySetHeaders`.
  - ConfigMap: Implement `dhParam`.
  - ConfigMap: Implement `tcp` and `udp`.
  - ConfigMap: Implement `controller.config`.
- Chart: Add KEDA resources. ([#413](https://github.com/giantswarm/ingress-nginx-app/pull/413))
- Chart: Add Prometheus rules. ([#414](https://github.com/giantswarm/ingress-nginx-app/pull/414))
- Chart: Add service monitor. ([#415](https://github.com/giantswarm/ingress-nginx-app/pull/415))

### Changed

- NetworkPolicy: Align to upstream. ([#408](https://github.com/giantswarm/ingress-nginx-app/pull/408))\
  **NOTE:** `controller.admissionWebhooks.networkPolicyEnabled` is being removed in favor of `controller.networkPolicy.enabled`.
- ConfigMap: Align to upstream. ([#409](https://github.com/giantswarm/ingress-nginx-app/pull/409))
  - ConfigMap: Align metadata.
  - ConfigMap: Rename `configmap.yaml` -> `controller-configmap.yaml`.
  - ConfigMap: Align indention.

## [2.24.1] - 2023-03-02

### Changed

- Webhook: Update digest to match last SHA. ([#421](https://github.com/giantswarm/ingress-nginx-app/pull/421))

## [2.24.0] - 2023-02-14

### Changed

- Change `PodDisruptionBudget` to move from `maxUnavailable: 1` to `maxUnavailable: 25%` for better scaling

## [2.23.2] - 2023-05-16

### Changed

- Jobs: Remove image digest.

## [2.23.1] - 2023-02-10

### Fixed

- Stop targeting default backend pods with the controller service. ([#402](https://github.com/giantswarm/ingress-nginx-app/pull/402))

## [2.23.0] - 2023-02-02

### Added

- Align to upstream: Allow configuring the default backend.

## [2.22.2] - 2023-05-16

### Changed

- Jobs: Remove image digest.

## [2.22.1] - 2023-01-18

### Added

- Metrics: Add `app.kubernetes.io/component` to selector. ([#393](https://github.com/giantswarm/ingress-nginx-app/pull/393))

### Removed

- HPA: Remove `controller.autoscaling.apiVersion`, use capabilites instead. ([#392](https://github.com/giantswarm/ingress-nginx-app/pull/392))

## [2.22.0] - 2023-01-17

### Added

- Service: Add CAPA support. ([#380](https://github.com/giantswarm/ingress-nginx-app/pull/380))
- Webhook: Use `cert-manager` for certificate lifecycle management. ([#386](https://github.com/giantswarm/ingress-nginx-app/pull/386))
- HPA: Make `apiVersion` configurable. ([#387](https://github.com/giantswarm/ingress-nginx-app/pull/387))
- Metrics: Align to upstream. ([#388](https://github.com/giantswarm/ingress-nginx-app/pull/388))
  - Values: Align to upstream.
  - Service: Make optional, enabled by default.
  - Service: Implement `controller.metrics.service.annotations`.
  - Service: Implement `controller.metrics.service.type`.
  - Service: Implement `controller.metrics.service.clusterIP`.
  - Service: Implement `controller.metrics.service.externalIPs`.
  - Service: Implement `controller.metrics.service.loadBalancerIP`.
  - Service: Implement `controller.metrics.service.loadBalancerSourceRanges`.
  - Service: Implement `controller.metrics.service.externalTrafficPolicy`.
  - Service: Implement `controller.metrics.portName`.
  - Service: Implement `controller.metrics.service.nodePort`.

### Changed

- Metrics: Align to upstream. ([#388](https://github.com/giantswarm/ingress-nginx-app/pull/388))
  - Service: Rename `controller-metrics-service.yaml` -> `controller-service-metrics.yaml`.
  - Service: Align labels to upstream.
  - Service: Order `name` & `namespace`.
  - Service: Rename from `-monitoring` to `-metrics`.
  - Service: Align indention of `ports`.

## [2.21.1] - 2023-05-16

- Jobs: Remove image digest. ([#485](https://github.com/giantswarm/ingress-nginx-app/pull/485))

## [2.21.0] - 2023-01-02

### Added

- HPA: Align to upstream. ([#369](https://github.com/giantswarm/ingress-nginx-app/pull/369))
  - HPA: Add labels & annotations.
  - HPA: Add `controller.kind` switch.
  - HPA: Add `controller.autoscalingTemplate`.
  - HPA: Add `controller.autoscaling.behavior`.
  - HPA: Add all KEDA values.
- PDB: Add `minAvailable`. ([#373](https://github.com/giantswarm/ingress-nginx-app/pull/373))
- Webhook: Align to upstream. ([#374](https://github.com/giantswarm/ingress-nginx-app/pull/374))
  - Webhook: Add `controller.admissionWebhooks.service.clusterIP`.
  - Webhook: Add `controller.admissionWebhooks.service.externalIPs`.
  - Webhook: Add `controller.admissionWebhooks.service.loadBalancerIP`.
  - Webhook: Add `controller.admissionWebhooks.service.loadBalancerSourceRanges`.
- Ingress Class: Align to upstream. ([#377](https://github.com/giantswarm/ingress-nginx-app/pull/377))
  - Ingress Class: Add `controller.ingressClass`.
- RBAC: Align to upstream. ([#378](https://github.com/giantswarm/ingress-nginx-app/pull/378))
  - Values: Add RBAC & service account configuration.
  - Helpers: Add `ingress-nginx.serviceAccountName`.
  - Values: Add `controller.electionID`.
  - Helpers: Add `podSecurityPolicy.apiGroup`.
  - Values: Add `controller.existingPsp`.
  - Values: Add `controller.hostNetwork` & `controller.hostPort`.
  - Values: Add `controller.image.chroot`.
  - Values: Add `controller.sysctls`.
  - Values: Add `controller.metrics.enabled` & `controller.metrics.portName`.
  - Values: Add `tcp` & `udp`.

### Changed

- HPA: Align to upstream. ([#369](https://github.com/giantswarm/ingress-nginx-app/pull/369))
  - HPA: Reorder name & namespace.
  - HPA: Use `ingress-nginx.controller.fullname`.
  - HPA: Use `autoscaling/v2beta2`.
  - HPA: Fix indention.
  - HPA: Swap CPU & memory block.
  - HPA: Disable when KEDA is enabled.
- Admission Webhooks: Align from upstream. ([#370](https://github.com/giantswarm/ingress-nginx-app/pull/370))
- Ingress Class: Align from upstream. ([#371](https://github.com/giantswarm/ingress-nginx-app/pull/371), [#374](https://github.com/giantswarm/ingress-nginx-app/pull/374), [#377](https://github.com/giantswarm/ingress-nginx-app/pull/377))
- Helpers: Rename `labels.selector` to `ingress-nginx.selectorLabels`. ([#372](https://github.com/giantswarm/ingress-nginx-app/pull/372))
- PDB: Align from upstream. ([#373](https://github.com/giantswarm/ingress-nginx-app/pull/373))
- Webhook: Align to upstream. ([#374](https://github.com/giantswarm/ingress-nginx-app/pull/374))
- RBAC: Align to upstream. ([#378](https://github.com/giantswarm/ingress-nginx-app/pull/378))
  - RBAC: Move `ClusterRoleBinding` to separate file.
  - RBAC: Move `RoleBinding` to separate file.
  - RBAC: Move `ClusterRole` to separate file.
  - RBAC: Move `Role` to separate file.
  - RBAC: Rename `service-account.yaml` to `controller-serviceaccount.yaml`.
  - RBAC: Rename `psp.yaml` to `controller-psp.yaml`.
  - RBAC: Move PSP `ClusterRoleBinding` to `clusterrolebinding.yaml`.
  - RBAC: Move PSP `ClusterRole` to `clusterrole.yaml`.
  - RBAC: Align `ServiceAccount`.
  - RBAC: Align `ClusterRoleBinding` to upstream.
  - RBAC: Align `ClusterRole` to upstream.
  - RBAC: Reorder `coordination.k8s.io/leases` in `ClusterRole`.
  - RBAC: Indent `ClusterRole`.
  - RBAC: Indent `Role`.
  - Helpers: Rename `controller.leader.election.id` to `ingress-nginx.controller.electionID`.
  - Helpers: Align `ingress-nginx.controller.electionID` to upstream.
  - RBAC: Align `Role` to upstream.
  - RBAC: Align `RoleBinding` to upstream.
  - RBAC: Move PSP `ClusterRole` & PSP `ClusterRoleBinding` to `Role`.
  - RBAC: Reorder & indent `PodSecurityPolicy`.
  - RBAC: Align `PodSecurityPolicy` to upstream.

## [2.20.1] - 2023-05-16

### Changed

- Jobs: Remove image digest. ([#482](https://github.com/giantswarm/ingress-nginx-app/pull/482))

## [2.20.0] - 2022-11-02

### Added

- Templates: Add `controller.admissionWebhooks.patch.labels`. ([#360](https://github.com/giantswarm/ingress-nginx-app/pull/360))
- Templates: Add `controller.admissionWebhooks.annotations`. ([#362](https://github.com/giantswarm/ingress-nginx-app/pull/362))
- Webhook: Add labels & selectors. ([#364](https://github.com/giantswarm/ingress-nginx-app/pull/364))
- Templates: Add `controller.admissionWebhooks.existingPsp`. ([#365](https://github.com/giantswarm/ingress-nginx-app/pull/365))
- Webhook: Align values & functions. ([#366](https://github.com/giantswarm/ingress-nginx-app/pull/366))
  - Webhook: Rename & align `NetworkPolicy`.
  - Helpers: Add `ingress-nginx.controller.fullname`.
  - Webhook: Add `controller.admissionWebhooks.extraEnvs`.
  - Webhook: Add `controller.admissionWebhooks.createSecretJob.resources`.
  - Webhook: Add `controller.admissionWebhooks.patchWebhookJob.resources`.
  - Webhook: Add `controller.admissionWebhooks.patch.securityContext`.

### Changed

- Helpers: Rename `resource.default.name` to `ingress-nginx.fullname`. ([#356](https://github.com/giantswarm/ingress-nginx-app/pull/356))
- Repository: Rename `master` to `main`. ([#357](https://github.com/giantswarm/ingress-nginx-app/pull/357))
- Helpers: Rename `labels.common` to `ingress-nginx.labels`. ([#358](https://github.com/giantswarm/ingress-nginx-app/pull/358))
- Templates: Align hook annotations, namespaces & indention. ([#359](https://github.com/giantswarm/ingress-nginx-app/pull/359), [#361](https://github.com/giantswarm/ingress-nginx-app/pull/361))
- Templates: Align `ValidatingWebhookConfiguration`. ([#363](https://github.com/giantswarm/ingress-nginx-app/pull/363))
- Webhook: Align values & functions. ([#366](https://github.com/giantswarm/ingress-nginx-app/pull/366))
  - Webhook: Disable privilege escalation.
  - Webhook: Align image concatenation.
  - Webhook: Align values.yaml.

### Removed

- Webhook: Align values & functions. ([#366](https://github.com/giantswarm/ingress-nginx-app/pull/366))
  - Webhook: Remove `controller.admissionWebhooks.patch.backoffLimit`. \
    `backoffLimit` was set to the default value of 6 all the time anyway, so we remove it to ease future upstream alignments.
- Revert 'Add support to create internal Load Balancers on GCP.'. ([#367](https://github.com/giantswarm/ingress-nginx-app/pull/367))

## [2.19.0] - 2022-10-17

### Added

- Add support to create internal Load Balancers on GCP.

### Changed

- Update controller container image to [`v1.4.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#140). ([#353](https://github.com/giantswarm/ingress-nginx-app/pull/353))

### Removed

- Disable `PodSecurityPolicy` for Kubernetes >= v1.25. ([#352](https://github.com/giantswarm/ingress-nginx-app/pull/352))

### Important notes

Please upgrade to any `v2.18.x` version before upgrading to this release or above since the controller image contained in there migrates your setup to the Lease API.

Additionally the controller version included in this release deprecates some metric names and introduces others as a replacement. See [this PR](https://github.com/kubernetes/ingress-nginx/pull/8728) and [the upstream docs](https://github.com/kubernetes/ingress-nginx/blob/controller-v1.4.0/docs/user-guide/monitoring.md#exposed-metrics) for more details.

## [2.18.2] - 2022-10-17

### Changed

- Update controller container image to [`v1.3.1`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#131). ([#349](https://github.com/giantswarm/ingress-nginx-app/pull/349))

## [2.18.1] - 2022-09-29

### Added

- Validation for `controller.service.externalTrafficPolicy` and `controller.service.internal.externalTrafficPolicy` to only allow `Local` and `Cluster`. ([#344](https://github.com/giantswarm/ingress-nginx-app/pull/344))

## [2.18.0] - 2022-09-27

### Added

- `controller.service.loadBalancerSourceRanges` & `controller.service.internal.loadBalancerSourceRanges` for configuring source IP address ranges which can access the ingress service.

## [2.17.0] - 2022-09-13

### Changed

- Enable `configmap.use-proxy-protocol` by default for AWS. Hint: Before this was achieved by `cluster-operator` setting `configmap.use-proxy-protocol` in the cluster values.

## [2.16.0] - 2022-08-24

This release removes support for Kubernetes v1.19.0 and adds support for Kubernetes v1.24.0

### Changed

- Update controller container image to [`v1.3.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#130). ([#335](https://github.com/giantswarm/ingress-nginx-app/pull/335))
- Increase default replica count to 2. ([#335](https://github.com/giantswarm/ingress-nginx-app/pull/335))

## [2.15.2] - 2022-08-15

### Added

- Support for labels on the controller metrics service.

## [2.15.1] - 2022-08-08

### Changed

- Update initContainer v3.15.5

## [2.15.0] - 2022-08-03

### Added

- Support for annotations, labels and suffix on the internal controller service.\
  **NOTE:** Adding, changing or removing the `suffix` results in a different name of the controller service resource. Since Helm does not keep track of the old resource, we recommend to uninstall and reinstall the app when changing the suffix.

### Changed

- Aligned internal controller service and its configuration parameters to the normal one.
- Omit `service.beta.kubernetes.io/aws-load-balancer-proxy-protocol` for `use-proxy-protocol: "false"`.

## [2.14.0] - 2022-06-24

### Changed

- externalDNS annotations won't no longer be set on the ingress services if `baseDomain` is not set. ([#321](https://github.com/giantswarm/ingress-nginx-app/pull/321))

### Removed

- Default value for `baseDomain` configuration value automatically set for workload cluster installations. ([#321](https://github.com/giantswarm/ingress-nginx-app/pull/321))
- Unused configuration values for chart installations on management clusters. ([#321](https://github.com/giantswarm/ingress-nginx-app/pull/321))

## [2.13.1] - 2022-06-16

### Changed

- Enable topology spread constraints by default. ([#318](https://github.com/giantswarm/ingress-nginx-app/pull/318))

## [2.13.0] - 2022-06-15

### Added

- Allow users to specify custom `nodeAffinity` configuration through `controller.nodeAffinity` configuration value. ([#313](https://github.com/giantswarm/ingress-nginx-app/pull/313))
- Optional: Topology spread constraints for pod assignment (requires Kubernetes >= 1.19). Ref: https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints. Important: We strongly suggest you review these settings before applying onto your clusters. This document https://docs.giantswarm.io/advanced/high-availability/multi-az/ gives more insight.

## [2.12.1] - 2022-06-09

### Changed

- Update controller container image to [`v1.2.1`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#121) which removes the root and alias directives from the internal NGINX. ([#311](https://github.com/giantswarm/ingress-nginx-app/pull/311))

## [2.12.0] - 2022-05-13

### Changed

- Reduced default resource requests to former profile `small` (at least 500m of CPU and 600Mi of memory) and let HPA care about scaling.

### Removed

- Support for `cluster.profile` parameter. This parameter was not set on either management clusters nor workload clusters and so the default resource requests configured in `controller.resources` got used.

## [2.11.0] - 2022-04-22

### Changed

- Update controller container image to [`v1.2.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#120) which enables deep inspection on Ingress objects. This may increase CPU usage slightly. ([#301](https://github.com/giantswarm/ingress-nginx-app/pull/301))

## [2.10.0] - 2022-04-04

### Added

- Controller flag `--ingress-class` to use configuration value `controller.ingressClassResource.name`. This enables backwards compatibility with `kubernetes.io/ingress.class` annotations on `Ingresses`. ([#292](https://github.com/giantswarm/ingress-nginx-app/pull/292))
- Configuration value `ingressClassByName` to enable or disable processing `IngressClass` per name (additionally as per spec.controller) (Default: `false`). ([#292](https://github.com/giantswarm/ingress-nginx-app/pull/292))

### Changed

- Added team ownership to default labels.
- Update controller container image to [`v1.1.3`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#113) to fix [CVE-2022-0778](https://github.com/kubernetes/ingress-nginx/issues/8339) in OpenSSL and [CVE-2022-23308](https://github.com/kubernetes/ingress-nginx/issues/8321) in libxml2. It also upgrades Alpine to 3.14.4 and nginx to 1.19.10. ([#292](https://github.com/giantswarm/ingress-nginx-app/pull/292))

## [2.9.1] - 2022-02-23

### Added

- Added `maxSurge` parameter to values for the controller deployment strategy.

## [2.9.0] - 2022-02-10

### Added

- Allow enabling the `--enable-ssl-chain-completion` flag. Disabled by default. Use this to autocomplete SSL certificate chains with missing intermediate CA certificates. Certificates uploaded to Kubernetes must have the "Authority Information Access" X.509 v3 extension for this to succeed.

## [2.8.0] - 2022-01-27

This release contains a potential breaking change in case you are using and relying on the configuration setting [`use-forwarded-headers`](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#use-forwarded-headers). From now on the default value will change to `false`. In case you're relying on this feature, you'll need override this in your customized values like this:

    configmap:
        use-forwarded-headers: "true"


### Changed

- Push chart to control plane catalog.
- Disable `use-forwarded-headers` by default.

## [2.7.0] - 2022-01-19

### Added

- Allow disabling external-dns annotations.
- Augment monitoring annotations to have a stable name for monitoring. ([#263](https://github.com/giantswarm/ingress-nginx-app/pull/263))
- Update aws-load-balancer annotations for internal cluster use.
- Add required external-dns annotation to internal controller service.
- Add documentation for service configuration.

### Changed

- Update controller container image to [`v1.1.1`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#111). ([#264](https://github.com/giantswarm/ingress-nginx-app/pull/264))
- Swap kube-webhook-certgen container image for ingress-nginx image to ensure compatibility with kubernetes >= 1.22 ([#265](https://github.com/giantswarm/ingress-nginx-app/pull/265))

## [2.6.1] - 2021-12-03

### Fixed

- Fix LB Service name suffix introduced in v2.6.0.

## [2.6.0] - 2021-12-02

:warning: This release is broken. Please use v2.6.1 instead.

### Added

- Allow setting LB Service name suffix with new `controller.service.suffix`
  value.

## [2.5.0] - 2021-11-29

### Changed

- Update controller container image to [`v1.1.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#110). ([#246](https://github.com/giantswarm/ingress-nginx-app/pull/246))

## [2.4.1] - 2021-10-22

### Changed

- Internal change: Stop publishing nginx-ingress-controller-app to default catalog. ([#235](https://github.com/giantswarm/ingress-nginx-app/pull/235))
- Disallow the controller Ingress to parse and add *-snippet annotations created by the user. This can be changed by setting `controller.allowSnippetAnnotations` to `true`.
  We recommend enabling this option only if you TRUST users with permission to create Ingress objects, as this may allow a user to add restricted configurations to the final nginx.conf file.
  This is a mitigation against CVE-2021-25742.
  ([#238](https://github.com/giantswarm/ingress-nginx-app/pull/238))

## [2.4.0] - 2021-10-18

### Changed

- Update controller container image to [`v1.0.4`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#104) which disables ssl_session_cache due to possible memory fragmentation. ([#231](https://github.com/giantswarm/ingress-nginx-app/pull/231))

## [2.3.0] - 2021-10-07

### Changed

- Update controller container image to [`v1.0.3`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#103) which resolves issues related to lua modules used in the controller. ([#225](https://github.com/giantswarm/ingress-nginx-app/pull/225))

## [2.2.0] - 2021-09-09

### Changed

- **Breaking change** Update controller container image to [`v1.0.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#100). From this version on, only clusters with kubernetes >= 1.19 are supported. Please make sure to read the [upgrading notes](https://github.com/giantswarm/ingress-nginx-app/blob/main/README.md#upgrading-notes). ([#218](https://github.com/giantswarm/ingress-nginx-app/pull/218)).

## [2.1.4] - 2022-04-07

### Changed

- Update controller container image to [`v0.51.0`](https://github.com/kubernetes/ingress-nginx/blob/legacy/Changelog.md#0510) to fix [CVE-2022-0778](https://github.com/kubernetes/ingress-nginx/issues/8339) in OpenSSL and [CVE-2022-23308](https://github.com/kubernetes/ingress-nginx/issues/8321) in libxml2. It also upgrades Alpine to 3.14.4 and nginx to 1.19.10. ([#294](https://github.com/giantswarm/ingress-nginx-app/pull/294))
- Added team ownership to default labels. ([#294](https://github.com/giantswarm/ingress-nginx-app/pull/294))

## [2.1.3] - 2021-12-20

### Changed

- Update controller container image to [`v0.50.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0500). ([#259](https://github.com/giantswarm/ingress-nginx-app/pull/259))

## [2.1.2] - 2021-10-22

### Changed

- Disallow the controller Ingress to parse and add *-snippet annotations/directives created by the user. This can be changed by setting `controller.enableSnippetDirectives` to `true`.
  We recommend enabling this option only if you TRUST users with permission to create Ingress objects, as this may allow a user to add restricted configurations to the final nginx.conf file.
  This is a mitigation against CVE-2021-25742.
  ([#237](https://github.com/giantswarm/ingress-nginx-app/pull/237))

## [2.1.1] - 2021-10-21

### Changed

- Update controller container image to [`v0.49.3`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0493). ([#228](https://github.com/giantswarm/ingress-nginx-app/pull/228))

## [2.1.0] - 2021-08-26

### Changed

- Update controller container image to [`v0.49.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0490). ([#216](https://github.com/giantswarm/ingress-nginx-app/pull/216))

## [2.0.0] - 2021-07-15

### Changed

Note: This upgrade is only a breaking change in the unlikely event that you have been specifying services as `externalName` with your Ingress as a backend. Otherwise, it is **not** a breaking change.

- Update controller container image to [`v0.48.1`](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v0.48.1). ([#211](https://github.com/giantswarm/ingress-nginx-app/pull/211)). This release contains several performance improvements related to the admission webhook.
- Potentially Breaking: Define `--disable-svc-external-name` flag by default to disable forwarding traffic to [ExternalName Services](https://kubernetes.io/docs/concepts/services-networking/service/#externalname). If you require this feature, you can enable forwarding again through setting `controller.disableExternalNameForwarding: false` in user values. ([#211](https://github.com/giantswarm/ingress-nginx-app/pull/211))

## [1.17.0] - 2021-06-16

### Changed

- Update controller container image to [`v0.47.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0470). ([#204](https://github.com/giantswarm/ingress-nginx-app/pull/204))

## [1.16.1] - 2021-04-20

### Added

- Pass through annotations and labels to the controller service

## [1.16.0] - 2021-04-15

### Fixed

- Fixes validation of cpu requests and limits to allow for string and integer values.
- Update controller container image to [`v0.45.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0450) to correct OpenSSL CVEs. ([#188](https://github.com/giantswarm/ingress-nginx-app/pull/188))
- Change monitoring service port to `10254`. ([#188](https://github.com/giantswarm/ingress-nginx-app/pull/188))

## [1.15.1] - 2021-04-01

### Added

- Add configuration options for `failurePolicy` and `timeoutSeconds` of validating webhook configuration. ([#186](https://github.com/giantswarm/ingress-nginx-app/pull/186))

## [1.15.0] - 2021-03-01

### Changed

- Update controller container image to [`v0.44.0`](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md)  and kube-webhook-certgen container image to 1.5.1. ([#179](https://github.com/giantswarm/ingress-nginx-app/pull/179))
- Remove conflicting admission webhook api versions. ([#178](https://github.com/giantswarm/ingress-nginx-app/pull/178))
- Remove unecessary annotation. ([#180](https://github.com/giantswarm/ingress-nginx-app/pull/180))

## [1.14.1] - 2021-02-09

### Changed

- Allow wildcard subdomains to be used in the external-dns annotation. ([#174](https://github.com/giantswarm/ingress-nginx-app/pull/174))

## [1.14.0] - 2021-02-03

### Added

- Add annotation to controller service for external-dns to use for filtering resources. ([#169](https://github.com/giantswarm/ingress-nginx-app/pull/169))
- Support user-provided annotations for the controller deployment. ([#170](https://github.com/giantswarm/ingress-nginx-app/pull/170))

## [1.13.0] - 2021-01-27

### Changed

- Update image to `v0.43.0`. ([#165](https://github.com/giantswarm/ingress-nginx-app/pull/165))

## [1.12.0] - 2020-12-09

### Added

- Allow toggling of the `--update-status` flag. Disabling this feature stops NGINX IC from updating Ingress Loadbalancer status fields. ([#151](https://github.com/giantswarm/ingress-nginx-app/pull/151))

### Changed

- Add ability to set podAntiAffinity scheduling method via the values file. ([#146](https://github.com/giantswarm/ingress-nginx-app/pull/146))

## [1.11.0] - 2020-11-18

### Added

- Add ability to extend `nginx-ingress-controller`with specific values from appcatalog.
- User value validation through a values.schema.json file based on the current values.yaml.

### Changed

- Update image to `v0.41.2`. ([#133](https://github.com/giantswarm/ingress-nginx-app/pull/133))

## [1.10.0] - 2020-10-07

### Changed

- Upgrade ingress-nginx-controller from v0.35.0 to [v0.40.2](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0402).

  **Important** upstream changes to pay special attention to:

  - App/chart requires Kubernetes 1.16+ based platform release
    - It is recommended to change API group of Ingress resources from `extensions/v1beta1` to `networking.k8s.io/v1beta1` (available since Kubernetes 1.14)
  - Default configuration changes:
    - [`gzip-level`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/configmap.md#gzip-level) default changed from `5` to `1`
    - [`ssl-session-tickets`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/configmap.md#ssl-session-tickets) default changed from `true` to `false`
    - [`use-gzip`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/configmap.md#use-gzip) default changed from `true` to `false`
    - [`upstream-keepalive-connections`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/configmap.md#upstream-keepalive-connections) changed from `32` to `320`
    - [`upstream-keepalive-requests`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/configmap.md#upstream-keepalive-requests) changed from `100` to `10000`
- Support and enable by default [mimalloc](https://github.com/microsoft/mimalloc) as a drop-in malloc replacement to reduce nginx memory utilization.
- Support configuring additional environment variables for NGINX Ingress Controller container, to support configuring additional mimalloc [options](https://github.com/microsoft/mimalloc#environment-options).
- Adjust Helm `hook-delete-policy` and `hook-weight` to make admission webhook management more reliable.

## [1.9.2] - 2020-09-02

### Added

- `giantswarm.io/monitoring` label (in addition to existing annotation) for
  the new sharded TC Prometheus to pick up the service.

### Changed

- Upgrade to ingress-nginx [v0.35.0](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0350).

## [1.9.1] - 2020-08-14

- Configure explicit helm hook weights to make validating webhook resource management reliable.

## [1.9.0] - 2020-08-13

- Support Ingress resources validating webhook.

## [1.8.4] - 2020-08-06

### Fixed

- Fix NetworkPolicy templating, to allow Pod ingress traffic (Prometheus scrape requests) on same port that the metrics/monitoring service advertises.

## [1.8.3] - 2020-07-31

### Fixed

- Fix controller RBAC permissions, granting "get" and "update" of leader election ConfigMap lock.

## [1.8.2] - 2020-07-31

### Fixed

- Fix controller RBAC permissions, granting "get" and "update" of leader election ConfigMap lock.

## [1.8.1] - 2020-07-28

### Added

- Make node ports configurable for NodePort Service type.

## [1.8.0] - 2020-07-24

### Breaking changes

In older releases the NGINX IC LoadBalancer Service name was hardcoded to `nginx-ingress-controller`. As of this release, to ensure the Service name uniqueness for multiple NGINX ICs per cluster support, the LoadBalancer Service name was made to be dynamic, derived from Helm release i.e. App Custom Resource (CR) name. Therefore, if you're upgrading from an older NGINX IC App release to v1.8.0+, existing NGINX IC LoadBalancer Service may get replaced by a new one for every NGINC IC App CR whose name is not `nginx-ingress-controller`.

When NGINX IC LoadBalancer Service gets recreated, cloud service provider (CSP) load balancer behind it gets recycled as well. It can take minute or so for ingress DNS records to be updated by `external-dns` and change propagated to clients. During that time there's ingress traffic downtime, since clients still resolve old no longer present CSP load balancer.

**Please take the potential ingress downtime (a minute or so) into consideration when planning the NGINX IC App upgrade from older to v1.8.0+.**

To make sure the downtime is shortest possible, external-dns availability is important precondition.
In recent platform releases (Azure v12.0.2, and AWS v12.1.4 and v11.5.4) we've improved external-dns monitoring and alerting.

**Therefore, before upgrading NGINX IC optional app to v1.8.0+, please make sure that your cluster has been upgraded to the latest platform release.**

### Added

- Support multiple NGINX IC App installations per tenant cluster.

### Removed

- Dropped support for deprecated configuration properties:
  - `configmap.annotations-prefix`
  - `configmap.default-ssl-certificate`
  - `configmap.hpa-enabled`
  - `configmap.hpa-max-replicas`
  - `configmap.hpa-min-replicas`
  - `configmap.hpa-target-cpu-utilization-percentage`
  - `configmap.hpa-target-memory-utilization-percentage`
  - `configmap.ingress-class`

## [1.7.3] - 2020-07-16

### Changed

- Upgrade to ingress-nginx [v0.34.1](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0341).

## [1.7.2] 2020-07-10

### Changed

- Upgrade to ingress-nginx [v0.34.0](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0340).

## [1.7.1] 2020-07-07

### Changed

- Support additional Service, for internal traffic. Existing Service can still be configured to be either for public (default) or internal traffic.
- Make monitoring headless Service non-optional.
- Enable managed app monitoring via monitoring service.

## [1.7.0] 2020-06-29

### Changed

- Use LoadBalancer Service on Azure.
- Change controller.service.type to LoadBalancer/NodePort, and introduce controller.service.public for public/internal service classification.
- Upgrade to ingress-nginx [0.33.0](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0330).

## [1.6.12] 2020-06-04

### Changed

- Make healthcheck probes configurable.
- Make liveness probe more resilient.

## [1.6.11] 2020-05-26

### Changed

- Align labels, use `app.kubernetes.io/name` instead of `k8s-app` where possible.
  `k8s-app` remains to be used for compatibility reasons, as selectors are not modifiable without recreating the Deployment.

## [1.6.10] 2020-04-29

### Changed

- Make NGINX IC Service `externalTrafficPolicy` configurable and default to `Local`.

## [1.6.9] 2020-04-22

### Changed

- Restrict PodSecurityPolicy volumes to only those required (removes wildcard).
- Tune `net.ipv4.ip_local_port_range` to `1024 65535` as a safe sysctl.
- Tune `net.core.somaxconn` to `32768` via an initContainer with privilege escalation.
- Use `4` worker processes by default.
- Use upstream default of max-worker-connections of `16384`.
- Ignore NGINX IC Deployment replica count configuration when HorizontalPodAutoscaler is enabled.
- Drop unnecessary Helm release revision annotation from NGINX IC Deployment.
- Adjust README for display in the web interface context.

## [1.6.8] 2020-04-09

### Changed

- Default `max-worker-connections` to `0`, making it same as `max-worker-open-files` i.e. `max open files (system's limit) / worker-processes - 1024`.
  This optimizes for high load conditions where it improves performance at the cost of increasing RAM utilization (even on idle).
- HorizontalPodAutoscaler was tuned to use `targetMemoryUtilizationPercentage` of `80` due to increased RAM utilization with new default for `max-worker-connections` of `0`.
- Removed use of `enable-dynamic-certificates` CLI flag, it has been deprecated since [ingress-nginx 0.26.0](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md#0260) via [ingress-nginx PR #4356](https://github.com/kubernetes/ingress-nginx/pull/4356)
- Changed default `error-log-level` from `error` to `notice`.
- Added a link to the README in the sources of Chart.yaml

## [1.6.7] 2020-04-08

### Changed

- Align graceful termination configuration with changes made in upstream ingress-nginx 0.26.0 (see [related PR #4487](https://github.com/kubernetes/ingress-nginx/pull/4487#issuecomment-525588554) and important section in [0.26.0 release notes](https://github.com/kubernetes/ingress-nginx/releases/tag/nginx-0.26.0)).
  - Make NGINX IC Deployment's `terminationGracePeriodSeconds` configurable and align its default with `configmap.worker-shutdown-timeout`
  - Make NGINX IC controller container lifecycle hooks configurable, and change from `sleep 60` to using `/wait-shutdown` as preStop hook.
- Make `controller.minReadySeconds` configurable.

## [1.6.6] 2020-04-01

### Changed

- Change deployment to use release revision not time for Helm 3 support.

## [1.6.5] 2020-03-23

### Changed

- Fix small cluster profile resource requests. ([#42](https://github.com/giantswarm/ingress-nginx-app/pull/42))

## [1.6.4] 2020-03-17

### Changed

- Disable HPA and PDB for xs clusters since NGINX Deployment resource requests are not set there. ([#40](https://github.com/giantswarm/ingress-nginx-app/pull/40))

## [1.6.3] 2020-03-16

### Changed

- Adjust resource requests, HPA and PDB depending on determined cluster profile; supported cluster profiles include xxs, xs, small, and larger than small or unknown. ([#38](https://github.com/giantswarm/ingress-nginx-app/pull/38))

  By default, for nginx on:
  - xxs clusters - clear resource requests, HPA and PDB are disabled
  - xs clusters - clear resource requests, enabled HPA and PDB
  - small clusters - have some resource requests, HPA and PDB are enabled
  - clusters larger than small or unknown - have decent resource requests i.e. capacity out-of-the-box, and HPA and PDB are enabled.

## [1.6.2] 2020-03-12

### Changed

- Reintroduced config properties which should have been just deprecated but got dropped prematurely in v1.4.0 ([#36](https://github.com/giantswarm/ingress-nginx-app/pull/36))
  - `configmap.annotations-prefix`
  - `configmap.default-ssl-certificate`
  - `configmap.hpa-enabled`
  - `configmap.hpa-max-replicas`
  - `configmap.hpa-min-replicas`
  - `configmap.hpa-target-cpu-utilization-percentage`
  - `configmap.hpa-target-memory-utilization-percentage`
  - `configmap.ingress-class`

## [1.6.1] 2020-03-10

### Changed

- Disable HPA, PDB and clear resource requests for extra small clusters. ([#34](https://github.com/giantswarm/ingress-nginx-app/pull/34))

## [1.6.0] 2020-02-28

### Changed

- Upgrade to nginx-ingress-controller 0.30.0. ([#31](https://github.com/giantswarm/ingress-nginx-app/pull/31))
- Configured app icon. ([#32](https://github.com/giantswarm/ingress-nginx-app/pull/32))
- Enabled HorizontalPodAutoscaler by default. ([#27](https://github.com/giantswarm/ingress-nginx-app/pull/27))
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

## [1.5.0] 2020-02-18

### Changed

- Disable nginx NodePort Service by default, having legacy cluster-operator enable it for legacy Azure only. ([#29](https://github.com/giantswarm/ingress-nginx-app/pull/29))
- Upgrade to nginx-ingress-controller 0.29.0. ([#30](https://github.com/giantswarm/ingress-nginx-app/pull/30))

## [1.4.0] 2020-02-10

### Changed

- Support overriding all nginx configmap settings. ([#26](https://github.com/giantswarm/ingress-nginx-app/pull/26))

## [1.3.0] 2020-01-30

### Changed

- Upgrade to nginx-ingress-controller 0.28.0. ([#24](https://github.com/giantswarm/ingress-nginx-app/pull/24))

## [1.2.1] 2020-01-29

### Changed

- Support proxy protocol for AWS. ([#23](https://github.com/giantswarm/ingress-nginx-app/pull/23))

## [1.2.0] 2020-01-21

### Changed

- Upgrade to nginx-ingress-controller 0.27.1. ([#20](https://github.com/giantswarm/ingress-nginx-app/pull/20))
- Add metrics Service for prometheus-operator support. ([#19](https://github.com/giantswarm/ingress-nginx-app/pull/19))
- Allow overriding of nginx SSL protocol default setting. ([#17](https://github.com/giantswarm/ingress-nginx-app/pull/17))

## [1.1.1] 2020-01-04

### Changed

- Updated manifests for Kubernetes 1.16. ([#16](https://github.com/giantswarm/ingress-nginx-app/pull/16))

## [1.1.0]

### Changed

- Migrate to managed application structure.

[kubernetes-nginx-ingress-controller](https://github.com/giantswarm/kubernetes-nginx-ingress-controller) repository is deprecated.

Previous versions changelog can be found [here](https://github.com/giantswarm/kubernetes-nginx-ingress-controller/blob/master/CHANGELOG.md)

[Unreleased]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.2.1...HEAD
[4.2.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.2.0...v4.2.1
[4.2.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.6...v4.2.0
[4.1.6]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.5...v4.1.6
[4.1.5]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.4...v4.1.5
[4.1.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.3...v4.1.4
[4.1.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.2...v4.1.3
[4.1.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.1...v4.1.2
[4.1.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.1.0...v4.1.1
[4.1.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.7...v4.1.0
[4.0.7]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.6...v4.0.7
[4.0.6]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.5...v4.0.6
[4.0.5]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.4...v4.0.5
[4.0.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.3...v4.0.4
[4.0.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.2...v4.0.3
[4.0.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.1...v4.0.2
[4.0.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.0...v4.0.1
[4.0.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v4.0.0-alpha1...v4.0.0
[4.0.0-alpha1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.8...v4.0.0-alpha1
[3.9.8]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.7...v3.9.8
[3.9.7]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.6...v3.9.7
[3.9.6]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.5...v3.9.6
[3.9.5]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.4...v3.9.5
[3.9.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.3...v3.9.4
[3.9.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.2...v3.9.3
[3.9.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.1...v3.9.2
[3.9.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.9.0...v3.9.1
[3.9.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.8.1...v3.9.0
[3.8.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.8.0...v3.8.1
[3.8.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.7.0...v3.8.0
[3.7.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.6.1...v3.7.0
[3.6.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.6.0...v3.6.1
[3.6.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.5.2...v3.6.0
[3.5.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.5.1...v3.5.2
[3.5.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.5.0...v3.5.1
[3.5.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.4.2...v3.5.0
[3.4.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.4.1...v3.4.2
[3.4.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.4.0...v3.4.1
[3.4.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.3.1...v3.4.0
[3.3.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.3.0...v3.3.1
[3.3.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.2.1...v3.3.0
[3.2.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.2.0...v3.2.1
[3.2.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.1.2...v3.2.0
[3.1.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.1.1...v3.1.2
[3.1.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.1.0...v3.1.1
[3.1.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.0.2...v3.1.0
[3.0.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.0.1...v3.0.2
[3.0.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.30.1...v3.0.0
[2.30.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.30.0...v2.30.1
[2.30.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.29.0...v2.30.0
[2.29.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.28.0...v2.29.0
[2.28.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.27.0...v2.28.0
[2.27.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.26.0...v2.27.0
[2.26.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.25.1...v2.26.0
[2.25.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.25.0...v2.25.1
[2.25.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.24.1...v2.25.0
[2.24.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.24.0...v2.24.1
[2.24.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.23.2...v2.24.0
[2.23.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.23.1...v2.23.2
[2.23.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.23.0...v2.23.1
[2.23.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.22.2...v2.23.0
[2.22.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.22.1...v2.22.2
[2.22.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.22.0...v2.22.1
[2.22.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.21.1...v2.22.0
[2.21.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.21.0...v2.21.1
[2.21.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.20.1...v2.21.0
[2.20.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.20.0...v2.20.1
[2.20.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.19.0...v2.20.0
[2.19.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.18.2...v2.19.0
[2.18.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.18.1...v2.18.2
[2.18.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.18.0...v2.18.1
[2.18.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.17.0...v2.18.0
[2.17.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.16.0...v2.17.0
[2.16.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.15.2...v2.16.0
[2.15.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.15.1...v2.15.2
[2.15.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.15.0...v2.15.1
[2.15.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.14.0...v2.15.0
[2.14.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.13.1...v2.14.0
[2.13.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.13.0...v2.13.1
[2.13.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.12.1...v2.13.0
[2.12.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.12.0...v2.12.1
[2.12.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.11.0...v2.12.0
[2.11.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.10.0...v2.11.0
[2.10.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.9.1...v2.10.0
[2.9.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.9.0...v2.9.1
[2.9.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.8.0...v2.9.0
[2.8.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.7.0...v2.8.0
[2.7.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.6.1...v2.7.0
[2.6.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.6.0...v2.6.1
[2.6.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.5.0...v2.6.0
[2.5.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.4.1...v2.5.0
[2.4.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.4.0...v2.4.1
[2.4.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.1.0...v2.2.0
[2.1.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.1.3...v2.1.4
[2.1.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.1.2...v2.1.3
[2.1.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.1.1...v2.1.2
[2.1.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.17.0...v2.0.0
[1.17.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.16.1...v1.17.0
[1.16.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.16.0...v1.16.1
[1.16.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.15.1...v1.16.0
[1.15.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.15.0...v1.15.1
[1.15.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.14.1...v1.15.0
[1.14.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.14.0...v1.14.1
[1.14.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.13.0...v1.14.0
[1.13.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.12.0...v1.13.0
[1.12.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.11.0...v1.12.0
[1.11.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.10.0...v1.11.0
[1.10.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.9.2...v1.10.0
[1.9.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.9.1...v1.9.2
[1.9.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.9.0...v1.9.1
[1.9.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.8.4...v1.9.0
[1.8.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.8.3...v1.8.4
[1.8.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.8.2...v1.8.3
[1.8.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.8.1...v1.8.2
[1.8.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.8.0...v1.8.1
[1.8.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.7.3...v1.8.0
[1.7.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.7.2...v1.7.3
[1.7.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.12...v1.7.0
[1.6.12]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.11...v1.6.12
[1.6.11]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.10...v1.6.11
[1.6.10]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.9...v1.6.10
[1.6.9]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.8...v1.6.9
[1.6.8]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.7...v1.6.8
[1.6.7]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.6...v1.6.7
[1.6.6]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.5...v1.6.6
[1.6.5]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.4...v1.6.5
[1.6.4]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.3...v1.6.4
[1.6.3]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.2...v1.6.3
[1.6.2]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.1...v1.6.2
[1.6.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.6.0...v1.6.1
[1.6.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/giantswarm/ingress-nginx-app/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/giantswarm/ingress-nginx-app/releases/tag/v1.1.0
