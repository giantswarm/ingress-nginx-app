[![CircleCI](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app.svg?style=svg)](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app)

# nginx-ingress-controller Helm Chart
Helm Chart for nginx-ingress-controller in Tenant Clusters.

* Installs the [nginx ingress controller](https://github.com/kubernetes/ingress-nginx).

## Installing the Chart

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

Deployment to Tenant Clusters is handled by [app-operator](https://github.com/giantswarm/app-operator).

## Configuration

Configuration options are documented in [Configuration.md](helm/nginx-ingress-controller-app/Configuration.md) document.

## Release Process

* Ensure CHANGELOG.md is up to date.
* Create a new GitHub release with the version e.g. `v0.1.0` and link the
changelog entry.
* This will push a new git tag and trigger a new tarball to be pushed to the
[default-catalog].  
* Update [cluster-operator] with the new version.

[app-operator]: https://github.com/giantswarm/app-operator
[cluster-operator]: https://github.com/giantswarm/cluster-operator
[default-catalog]: https://github.com/giantswarm/giantswarm-catalog
[default-test-catalog]: https://github.com/giantswarm/giantswarm-catalog-catalog
[nginx-ingress-controller]: https://github.com/kubernetes/ingress-nginx
