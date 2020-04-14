[![CircleCI](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app.svg?style=shield)](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app)

-----

**This readme documents an App on the Giant Swarm App Platform**

Read more in: [What is this repo?](#what-is-this-repo)

----

# nginx Ingress Controller App

This App installs the [nginx ingress controller] onto your tenant cluster.

Its job is to satisfy external requests to services running in the cluster. See the [kubernetes ingress docs] for more higher level details.

Some of our clusters do not come with an ingress controller installed by default, that way you can pick one of the implementations that best suits your needs. This is one of the more popular ingress controllers.

Ingress controllers watch the kubernetes api server's `/ingresses` endpoint for updates to the Ingress resource.

**Table of Contents:**

- [nginx Ingress Controller App](#nginx-ingress-controller-app)
- [Usage](#usage)
  - [Sample values files](#sample-values-files)
  - [Sample App CR and ConfigMap](#sample-app-cr-and-configmap)
- [Configuration](#configuration)
- [Limitations](#limitations)
- [For developers](#for-developers)
  - [Installing the Chart locally](#installing-the-chart-locally)
  - [Release Process](#release-process)
- [What is this repo?](#what-is-this-repo)


# Usage



## Sample values files

This is an example of the values file you could upload using our web interface.

```
# values.yaml

app: hello
yolo: bolo
```

If you are not using the web interface, our (deprecated) API takes the same structure but formatted as JSON:

```
# values.json

{
  "app": "hello",
  "yolo": "bolo",
}
```

## Sample App CR and ConfigMap

If you have access to the Kubernetes API on the Control Plane, you could create the App CR and ConfigMap directly. Here is an example:

```
# appCR.yaml

WIP
```

```
# user-values-configmap.yaml

WIP
```

If you feel like any of the configuration values need to be encrypted at rest, you can also provide a secret. For this app we don't think there are any configuration values that need to be encrypted.

If you place these files in a folder called `foldername`, you could use the command: `kubectl apply foldername`, to deploy this app to a tenant cluster with id `s4mpl`.

See our [full reference page on how to configure applications](https://docs.giantswarm.io/reference/app-configuration/) for more details.

# Configuration

The following table lists all the configuration options for this App. Refer to the examples above for how to set one of these values when installing your App.

Value | Description | Default
--- | --- | ---
`baseDomain` | Cluster base domain. Dynamically calculated during cluster creation. Manual change doesn't affect this value | 'uun5a.k8s.ginger.eu-central-1.aws.gigantic.io'
`clusterID` | Cluster ID. Dynamically calculated during cluster creation. Manual change doesn't affect this value | 'uun5a'
`cluster.profile` | Cluster usage profile. Dynamically calculated during cluster creation. Supported values are `1` for extra extra small, `2` for extra small, `3` for small, and currently any value higher than 3 when actual cluster profile is larger than small or unknown. By default HPA and PDB are disabled, and resource requests unset for extra extra small clusters and extra small clusters. On small clusters some small resource requests are made, HPA and PDB are enabled by default. On larger than small clusters HPA and PDB are enabled by default, and non-trivial resource requests set for some out-of-the-box guaranteed capacity. | `4`
`configmap` | Sets the nginx configmap configuration overrides. | See official docs for nginx [configmap configuration options](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/nginx-configuration/configmap.md#configuration-options) and their defaults. Built-in overrides are covered below.
`configmap.annotations-prefix` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.annotationsPrefix`. | not configured by default
`configmap.default-ssl-certificate` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.defaultSSLCertificate`. | not configured by default
`configmap.hpa-enabled` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.autoscaling.enabled`. | not configured by default
`configmap.hpa-max-replicas` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.autoscaling.maxReplicas`. | not configured by default
`configmap.hpa-min-replicas` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.autoscaling.minReplicas`. | not configured by default
`configmap.hpa-target-cpu-utilization-percentage` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.autoscaling.targetCPUUtilizationPercentage`. | not configured by default
`configmap.hpa-target-memory-utilization-percentage` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.autoscaling.targetMemoryUtilizationPercentage`. | not configured by default
`configmap.ingress-class` | This configuration property is deprecated and will be removed in the future, please migrate to `controller.ingressClass`. | not configured by default
`configmap.error-log-level` | Configures the logging level of errors. | "notice"
`configmap.hsts` | Enables or disables the HTTP Strict Transport Security (HSTS) header in servers running SSL. | "false"
`configmap.max-worker-connections` | Sets the maximum number of simultaneous connections that can be opened by each worker process. 0 will use the value of `max-worker-open-files`. | "0"
`configmap.max-worker-open-files` | Sets the maximum number of files that can be opened by each worker process. The default of 0 means "max open files (system's limit) / worker-processes - 1024". | "0"
`configmap.server-name-hash-bucket-size` | Sets the size of the bucket for the server names hash tables. | "1024"
`configmap.server-tokens` | Controlls whether to send NGINX Server header in responses and display NGINX version in error pages. | "false"
`configmap.worker-processes` | Sets the number of worker processes. | "1"
`configmap.worker-shutdown-timeout` | Maximum amount of time NGINX worker processes should give active connections to drain. This should not be higher than `controller.terminationGracePeriodSeconds` | "240s"
`configmap.use-forwarded-headers` | If true, NGINX passes the incoming `X-Forwarded-*` headers to upstreams. | "true"
`controller.annotationsPrefix` | Prefix of the Ingress annotations specific to the NGINX controller. This is a replacement for deprecated `configmap.annotations-prefix` configuration property; if both are configured, `configmap.annotations-prefix` has precedence. | `nginx.ingress.kubernetes.io`
`controller.autoscaling.enabled` | Enables or disables Horizontal Pod Autoscaler (HPA) for NGINX Ingress Controller Deployment. This is a replacement for deprecated `configmap.hpa-enabled` configuration property; if both are configured, `configmap.hpa-enabled` has precedence. | `true`
`controller.autoscaling.maxReplicas` | Configures HPA max replicas. This is a replacement for deprecated `configmap.hpa-max-replicas` configuration property; if both are configured, `configmap.hpa-max-replicas` has precedence. | `20`
`controller.autoscaling.minReplicas` | Configures HPA min replicas. This is a replacement for deprecated `configmap.hpa-min-replicas` configuration property; if both are configured, `configmap.hpa-min-replicas` has precedence. | `2`
`controller.autoscaling.targetCPUUtilizationPercentage` | Configures HPA target CPU utilization percentage. This is a replacement for deprecated `configmap.hpa-target-cpu-utilization-percentage` configuration property; if both are configured, `configmap.hpa-target-cpu-utilization-percentage` has precedence. | `50`
`controller.autoscaling.targetMemoryUtilizationPercentage` | Configures HPA target memory utilization percentage. This is a replacement for deprecated `configmap.hpa-target-memory-utilization-percentage` configuration property; if both are configured, `configmap.hpa-target-memory-utilization-percentage` has precedence. | `80`
`controller.defaultSSLCertificate` | The Secret referred to by this flag contains the default certificate to be used when accessing the catch-all server. If this flag is not provided NGINX will use a self-signed certificate. Example value: "default/foo-tls". This is a replacement for deprecated `configmap.default-ssl-certificate` configuration property; if both are configured, `configmap.default-ssl-certificate` has precedence. | ""
`controller.ingressController.legacy` | Legacy or node pools cluster. On aws provider node pool clusters LoadBalancer service gets created. Dynamically calculated during cluster creation. | `false`
`controller.ingressClass` | Ingress class, which controller handles. This is a replacement for deprecated `configmap.ingress-class` configuration property; if both are configured, `configmap.ingress-class` has precedence. | `nginx`
`controller.lifecycle` | Configures NGINX controller container lifecycle hooks. | By default configured to run `/wait-shutdown` as controller container preStop hook.
`controller.maxUnavailable` | Configures maximum unavailable replicas count for NGINX controller Deployment rolling upgrade strategy. | `1`
`controller.metrics.enabled` | If true, create metrics Service for prometheus-operator support. | `false`
`controller.metrics.port` | Configures container metrics port to be exposed. | `10254`
`controller.metrics.service.servicePort` | Configures metrics Service port. | `9913`
`controller.minReadySeconds` | Configures minimum amount of time that NGINX IC Deployment replica has to be ready before rolling upgrade can proceed with the next replica. | `0`
`controller.replicaCount` | Number of initial NGINX IC Deployment replicas. | `1`
`controller.service.enabled` | If true, create NodePort Service. Dynamically calculated during cluster creation. | `false`
`controller.service.type` | Applies only to `provider=aws` (`external`/`internal`) | `external`
`controller.terminationGracePeriodSeconds` | Maximum amount of time NGINX Deployment replica is given to gracefully terminate. This should not be lower than `configmap.worker-shutdown-timeout`. | 300
`provider` | Provider identifier (`aws`/`azure`/`kvm`) | `kvm`


# Limitations

Some of our apps have certain restrictions on how they can be deployed. Not following these limitations will most likely result in a broken deployment.

- This app _must_ be installed in the `kube-system` namespace.

- This app _must_ not be installed more than once.

# For developers

## Installing the Chart locally

To install the chart locally:

```bash
$ git clone https://github.com/giantswarm/nginx-ingress-controller-app.git
$ cd nginx-ingress-controller-app
$ helm install helm/nginx-ingress-controller-app
```

Provide a custom `values.yaml`:

```bash
$ helm install nginx-ingress-controller-app -f values.yaml
```

## Release Process

* Ensure CHANGELOG.md is up to date.
* Create a new GitHub release with the version e.g. `v0.1.0` and link the
changelog entry.
* This will push a new git tag and trigger a new tarball to be pushed to the
[giantswarm-catalog] and [default-catalog].
* Update [cluster-operator] with the new version.

# What is this repo?

This repo contains a helm chart for the [Giant Swarm App Platform].

This helm chart is available as an `App` in the `giantswarm-catalog` and `giantswarm-test-catalog`.

It is also availabe in the `default-catalog` and the `default-test-catalog`

While it is _just a Helm chart_, there might be some Giant Swarm App Platform specific values in the templates.

[app-operator]: https://github.com/giantswarm/app-operator
[cluster-operator]: https://github.com/giantswarm/cluster-operator
[giantswarm-catalog]: https://github.com/giantswarm/giantswarm-catalog
[giantswarm-test-catalog]: https://github.com/giantswarm/giantswarm-test-catalog
[default-catalog]: https://github.com/giantswarm/default-catalog
[default-test-catalog]: https://github.com/giantswarm/default-test-catalog
[nginx ingress controller]: https://github.com/kubernetes/ingress-nginx
[Giant Swarm App Platform]: https://docs.giantswarm.io/basics/app-catalog/
[Kubernetes Ingress docs]: https://kubernetes.io/docs/concepts/services-networking/ingress/