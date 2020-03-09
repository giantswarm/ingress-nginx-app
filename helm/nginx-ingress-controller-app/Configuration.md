# nginx-ingress-controller

This chart installs nginx-ingress-controller and its dependencies as managed applications. An Ingress Controller is a daemon, deployed as a Kubernetes Pod, that watches the apiserver's /ingresses endpoint for updates to the Ingress resource. Its job is to satisfy requests for Ingresses.

## Configuration

The following table lists the configurable parameters of the nginx-ingress-controller chart, its dependencies and default values.

Parameter | Description | Default
--- | --- | ---
`baseDomain` | Cluster base domain. Dynamically calculated during cluster creation. Manual change doesn't affect this value | 'uun5a.k8s.ginger.eu-central-1.aws.gigantic.io'
`clusterID` | Cluster ID. Dynamically calculated during cluster creation. Manual change doesn't affect this value | 'uun5a'
`cluster.profile` | Cluster usage profile. Dynamically calculated during cluster creation. `0` for unknown, `1` for extra small. HPA is disabled and resource requests unset for extra small clusters. | `0`
`configmap` | Sets the nginx configmap configuration overrides. | See official docs for nginx [configmap configuration options](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/nginx-configuration/configmap.md#configuration-options) and their defaults. Built-in overrides are covered below.
`configmap.error-log-level` | Configures the logging level of errors. | "error"
`configmap.hsts` | Enables or disables the HTTP Strict Transport Security (HSTS) header in servers running SSL. | "false"
`configmap.server-name-hash-bucket-size` | Sets the size of the bucket for the server names hash tables. | "1024"
`configmap.server-tokens` | Controlls whether to send NGINX Server header in responses and display NGINX version in error pages. | "false"
`configmap.worker-processes` | Sets the number of worker processes. | "1"
`configmap.use-forwarded-headers` | If true, NGINX passes the incoming `X-Forwarded-*` headers to upstreams. | "true"
`controller.annotationsPrefix` | Prefix of the Ingress annotations specific to the NGINX controller. | `nginx.ingress.kubernetes.io`
`controller.autoscaling.enabled` | Enables or disables Horizontal Pod Autoscaler (HPA) for NGINX Ingress Controller Deployment. | `true`
`controller.autoscaling.minReplicas` | Configures HPA min replicas. | `2`
`controller.autoscaling.maxReplicas` | Configures HPA max replicas. | `20`
`controller.autoscaling.targetCPUUtilizationPercentage` | Configures HPA target CPU utilization percentage. | `50`
`controller.autoscaling.targetMemoryUtilizationPercentage` | Configures HPA target memory utilization percentage. | `50`
`controller.defaultSSLCertificate` | The Secret referred to by this flag contains the default certificate to be used when accessing the catch-all server. If this flag is not provided NGINX will use a self-signed certificate. Example value: "default/foo-tls" | ""
`controller.ingressController.legacy` | Legacy or node pools cluster. On aws provider node pool clusters LoadBalancer service gets created. Dynamically calculated during cluster creation. | `false`
`controller.ingressClass` | Ingress class, which controller processes | `nginx`
`controller.metrics.enabled` | If true, create metrics Service for prometheus-operator support. | `false`
`controller.metrics.port` | Configures container metrics port to be exposed. | `10254`
`controller.metrics.service.servicePort` | Configures metrics Service port. | `9913`
`controller.replicaCount` | Number of initial NGINX Ingress Controller Deployment replicas. | `1`
`controller.service.enabled` | If true, create NodePort Service. Dynamically calculated during cluster creation. | `false`
`controller.service.type` | Applies only to `provider=aws` (`external`/`internal`) | `external`
`provider` | Provider identifier (`aws`/`azure`/`kvm`) | `kvm`
