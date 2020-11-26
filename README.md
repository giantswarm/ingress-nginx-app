[![CircleCI](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app.svg?style=shield)](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app)

-----

**This readme documents an App on the Giant Swarm App Platform**

Read more in: [What is this repo?](#what-is-this-repo)

----

# nginx Ingress Controller App

This App installs the [nginx ingress controller] onto your tenant cluster.

Its job is to satisfy external requests to services running in the cluster.
See the [kubernetes ingress docs] for a higher level overview.

Some of our clusters do not come with an ingress controller installed by default,
that way you can pick one of the implementations that best suits your needs.
This is one of the more popular ingress controllers.

Ingress controllers watch the kubernetes api server's `/ingresses` endpoint for
updates to the Ingress resource.

**Table of Contents:**

- [nginx Ingress Controller App](#nginx-ingress-controller-app)
- [Installing](#installing)
  - [Sample values files for the web interface and API](#sample-values-files-for-the-web-interface-and-api)
  - [Sample App CR and ConfigMap for the Control Plane](#sample-app-cr-and-configmap-for-the-control-plane)
  - [Important note about required cluster level config](#important-note-about-required-cluster-level-config)
- [Configuration Options](#configuration-options)
- [Limitations](#limitations)
- [For developers](#for-developers)
  - [Installing the Chart locally](#installing-the-chart-locally)
  - [Release Process](#release-process)
- [What is this repo?](#what-is-this-repo)


# Installing

There are 3 ways to install this app onto a tenant cluster.

1. [Using our web interface](https://docs.giantswarm.io/reference/web-interface/app-catalog/)
2. [Using our API](https://docs.giantswarm.io/api/#operation/createClusterAppV5)
3. Directly creating the App custom resource on the Control Plane.

## Sample values files for the web interface and API

This is an example of the values file you could upload using our web interface.

```
# values.yaml

configmap:
  error-log-level: info
```

If you are not using the web interface, our (deprecated) API takes the same
structure but formatted as JSON:

```
# values.json

{
  "configmap": {
    "error-log-level": "info"
  }
}
```

## Sample App CR and ConfigMap for the Control Plane

If you have access to the Kubernetes API on the Control Plane, you could create
the App CR and ConfigMap directly.

Here is an example that would install the nginx-ingress-controller-app to
tenant cluster `abc12`:

```
# appCR.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 1.0.0
  name: nginx-ingress-controller-app

  # Tenant cluster resources live in a namespace with the same ID as the
  # tenant cluster.
  namespace: abc12

spec:
  name: nginx-ingress-controller-app
  namespace: kube-system
  catalog: giantswarm
  version: 1.6.8

  userConfig:
    configMap:
      name: nginx-ingress-controller-app-user-values
      namespace: abc12
    secret:
      name: ""
      namespace: ""

  config:
    configMap:
      name: ingress-controller-values
      namespace: abc12
    secret:
      name: ""
      namespace: ""

  kubeConfig:
    context:
      name: abc12-kubeconfig
    inCluster: false
    secret:
      name: abc12-kubeconfig
      namespace: abc12
```

```
# user-values-configmap.yaml

apiVersion: v1
kind: ConfigMap

metadata:
  name: nginx-ingress-controller-app-user-values
  namespace: abc12

data:
  values: |
    configmap:
      error-log-level: info
```

If you feel like any of the configuration values need to be encrypted at rest,
you can also provide a secret. For this app we don't think there are any
configuration values that need to be encrypted.

It is a convention to call the user level configmap `{app-name}-user-values`.
So in this case we called the ConfigMap `nginx-ingress-controller-app-user-values`

If you place these files in a folder called `foldername`, you could use the
command: `kubectl apply foldername`, to deploy this app to a tenant cluster
with id `abc12`.

See our [full reference page on how to configure applications](https://docs.giantswarm.io/reference/app-configuration/) for more details.

## Important note about required cluster level config

The `ingress-controller-values` ConfigMap referenced in the `spec.config` field of the App CR
is required for the ingress controller to work properly.

`ingress-controller-values` is created by our operators and it helps set values
unique to your tenant cluster. When creating this App using our web interface or
our API, `spec.config` will be set automatically, but if you are creating the App CR
yourself you must remember to do this. We are working on a kubectl plugin to
facilitate this process.

# Configuration Options

All configuration options are documented in the [values.yaml](/helm/nginx-ingress-controller-app/values.yaml) file.

# Limitations

Some of our apps have certain restrictions on how they can be deployed.
Not following these limitations will most likely result in a broken deployment.

- This app _must_ reference the `ingress-controller-values` ConfigMap in its `spec.config` field.

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
* Test and verify the ingress controller release across supported environments in a new or existing WIP platform release.

# What is this repo?

This repo contains a helm chart for the [Giant Swarm App Platform].
While it is _just a Helm chart_, there might be some Giant Swarm App Platform
specific values in the templates.

It is available as an `App` in the `giantswarm-catalog` and `giantswarm-test-catalog`.

You will also find it in the `default-catalog` and the `default-test-catalog`,
those catalogs are not visible in our web interface. This is to support the
platforms and cluster versions where the nginx ingress controller is still a
default app (i.e. it gets installed automatically during cluster creation)

[app-operator]: https://github.com/giantswarm/app-operator
[giantswarm-catalog]: https://github.com/giantswarm/giantswarm-catalog
[giantswarm-test-catalog]: https://github.com/giantswarm/giantswarm-test-catalog
[default-catalog]: https://github.com/giantswarm/default-catalog
[default-test-catalog]: https://github.com/giantswarm/default-test-catalog
[nginx ingress controller]: https://github.com/kubernetes/ingress-nginx
[Giant Swarm App Platform]: https://docs.giantswarm.io/basics/app-catalog/
[Kubernetes Ingress docs]: https://kubernetes.io/docs/concepts/services-networking/ingress/
