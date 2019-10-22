[![CircleCI](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app.svg?style=shield)](https://circleci.com/gh/giantswarm/nginx-ingress-controller-app)

# nginx-ingress-controller

Helm Chart for Nginx Ingress Controller in Tenant Clusters.

* Installs the [nginx ingress controller].

## Deployment

* Managed by [app-operator].
* Production releases are stored in the [giantswarm-catalog].
* WIP releases are stored in the [giantswarm-test-catalog].

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

 ## Release Process

* Ensure CHANGELOG.md is up to date.
* Create a new GitHub release with the version e.g. `v0.1.0` and link the
changelog entry.
* This will push a new git tag and trigger a new tarball to be pushed to the
[giantswarm-catalog].  
* Update [cluster-operator] with the new version.

[app-operator]: https://github.com/giantswarm/app-operator
[cluster-operator]: https://github.com/giantswarm/cluster-operator
[giantswarm-catalog]: https://github.com/giantswarm/giantswarm-catalog
[giantswarm-test-catalog]: https://github.com/giantswarm/giantswarm-test-catalog
[nginx ingress controller]: https://github.com/kubernetes/ingress-nginx