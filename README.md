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

All configuration options are documented in the [values.yaml](/helm/nginx-ingress-controller-app/values.yaml) file.

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