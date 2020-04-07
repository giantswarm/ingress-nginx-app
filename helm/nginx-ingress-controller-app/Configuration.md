# nginx-ingress-controller

This chart installs nginx-ingress-controller and its dependencies as managed applications. An Ingress Controller is a daemon, deployed as a Kubernetes Pod, that watches the apiserver's /ingresses endpoint for updates to the Ingress resource. Its job is to satisfy requests for Ingresses.

## Configuration

The following table lists the configurable parameters of the nginx-ingress-controller chart, its dependencies and default values.

Parameter | Description | Default
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
`configmap.error-log-level` | Configures the logging level of errors. | "error"
`configmap.hsts` | Enables or disables the HTTP Strict Transport Security (HSTS) header in servers running SSL. | "false"
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
`controller.autoscaling.targetMemoryUtilizationPercentage` | Configures HPA target memory utilization percentage. This is a replacement for deprecated `configmap.hpa-target-memory-utilization-percentage` configuration property; if both are configured, `configmap.hpa-target-memory-utilization-percentage` has precedence. | `50`
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
