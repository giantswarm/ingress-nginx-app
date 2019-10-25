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
