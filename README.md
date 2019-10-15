# nginx-ingress-controller

This chart installs nginx-ingress-controller and its dependencies as managed applications. An Ingress Controller is a daemon, deployed as a Kubernetes Pod, that watches the apiserver's /ingresses endpoint for updates to the Ingress resource. Its job is to satisfy requests for Ingresses.

## Dependencies

### external-dns

ExternalDNS synchronizes exposed Kubernetes Services and Ingresses with DNS providers. In a broader sense, ExternalDNS allows you to control DNS records dynamically via Kubernetes resources in a DNS provider-agnostic way.

### kiam (applies to AWS provider only)

'kiam' runs as an agent on each node in your Kubernetes cluster and allows cluster users to associate IAM roles to Pods.


## Configuration

The following table lists the configurable parameters of the nginx-ingress-controller chart, its dependencies and default values.

Parameter | Description | Default
--- | --- | ---
`provider` | `aws`/`azure`/`kvm`. Taken from application catalog configuration. Can't be modified on chart level | `kvm`
`controller.service.enabled` | If true, create service | `true`
`controller.service.type` | Applied only for `provider=aws` (`external`/`internal`) | `external`
