# nginx-ingress-controller-app

![Version: 2.29.0](https://img.shields.io/badge/Version-2.29.0-informational?style=flat-square) ![AppVersion: 1.7.0](https://img.shields.io/badge/AppVersion-1.7.0-informational?style=flat-square)

Ingress controller for Kubernetes using NGINX as a reverse proxy and load balancer

**Homepage:** <https://github.com/giantswarm/nginx-ingress-controller-app>

## Source Code

* <https://github.com/kubernetes/ingress-nginx>

## Requirements

Kubernetes: `>=1.20.0-0`

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| baseDomain | string | `""` |  |
| commonLabels | object | `{}` |  |
| configmap.error-log-level | string | `"notice"` |  |
| configmap.hsts | string | `"false"` |  |
| configmap.server-name-hash-bucket-size | string | `"1024"` |  |
| configmap.use-forwarded-headers | string | `"false"` |  |
| configmap.worker-processes | string | `"4"` |  |
| configmap.worker-shutdown-timeout | string | `"240s"` |  |
| controller.addHeaders | object | `{}` | Will add custom headers before sending response traffic to the client according to: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#add-headers |
| controller.admissionWebhooks.annotations | object | `{}` |  |
| controller.admissionWebhooks.certManager.admissionCert.duration | string | `""` |  |
| controller.admissionWebhooks.certManager.enabled | bool | `false` |  |
| controller.admissionWebhooks.certManager.rootCert.duration | string | `""` |  |
| controller.admissionWebhooks.certificate | string | `"/usr/local/certificates/cert"` |  |
| controller.admissionWebhooks.createSecretJob.resources | object | `{}` |  |
| controller.admissionWebhooks.createSecretJob.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| controller.admissionWebhooks.enabled | bool | `true` |  |
| controller.admissionWebhooks.existingPsp | string | `""` | Use an existing PSP instead of creating one |
| controller.admissionWebhooks.extraEnvs | list | `[]` | Additional environment variables to set |
| controller.admissionWebhooks.failurePolicy | string | `"Fail"` | Admission Webhook failure policy to use |
| controller.admissionWebhooks.key | string | `"/usr/local/certificates/key"` |  |
| controller.admissionWebhooks.labels | object | `{}` | Labels to be added to admission webhooks |
| controller.admissionWebhooks.namespaceSelector | object | `{}` |  |
| controller.admissionWebhooks.objectSelector | object | `{}` |  |
| controller.admissionWebhooks.patch.enabled | bool | `true` |  |
| controller.admissionWebhooks.patch.image.digest | string | `""` |  |
| controller.admissionWebhooks.patch.image.image | string | `"giantswarm/ingress-nginx-kube-webhook-certgen"` |  |
| controller.admissionWebhooks.patch.image.pullPolicy | string | `"IfNotPresent"` |  |
| controller.admissionWebhooks.patch.image.tag | string | `"v20230312-helm-chart-4.5.2-28-g66a760794"` |  |
| controller.admissionWebhooks.patch.labels | object | `{}` | Labels to be added to patch job resources |
| controller.admissionWebhooks.patch.nodeSelector."kubernetes.io/os" | string | `"linux"` |  |
| controller.admissionWebhooks.patch.podAnnotations | object | `{}` |  |
| controller.admissionWebhooks.patch.priorityClassName | string | `""` | Provide a priority class name to the webhook patching job # |
| controller.admissionWebhooks.patch.securityContext.fsGroup | int | `2000` |  |
| controller.admissionWebhooks.patch.securityContext.runAsNonRoot | bool | `true` |  |
| controller.admissionWebhooks.patch.securityContext.runAsUser | int | `2000` |  |
| controller.admissionWebhooks.patch.tolerations | list | `[]` |  |
| controller.admissionWebhooks.patchWebhookJob.resources | object | `{}` |  |
| controller.admissionWebhooks.patchWebhookJob.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| controller.admissionWebhooks.port | int | `8443` |  |
| controller.admissionWebhooks.service.annotations | object | `{}` |  |
| controller.admissionWebhooks.service.externalIPs | list | `[]` |  |
| controller.admissionWebhooks.service.loadBalancerSourceRanges | list | `[]` |  |
| controller.admissionWebhooks.service.servicePort | int | `443` |  |
| controller.admissionWebhooks.service.type | string | `"ClusterIP"` |  |
| controller.affinity | object | `{}` | Affinity and anti-affinity rules for server scheduling to nodes # Ref: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity # |
| controller.allowSnippetAnnotations | bool | `false` | This configuration defines if Ingress Controller should allow users to set their own *-snippet annotations, otherwise this is forbidden / dropped when users add those annotations. Global snippets in ConfigMap are still respected |
| controller.annotations | object | `{}` | Annotations to be added to the controller Deployment or DaemonSet # |
| controller.annotationsPrefix | string | `"nginx.ingress.kubernetes.io"` |  |
| controller.autoscaling.annotations | object | `{}` |  |
| controller.autoscaling.behavior | object | `{}` |  |
| controller.autoscaling.enabled | bool | `true` |  |
| controller.autoscaling.maxReplicas | int | `20` |  |
| controller.autoscaling.minReplicas | int | `2` |  |
| controller.autoscaling.targetCPUUtilizationPercentage | int | `50` |  |
| controller.autoscaling.targetMemoryUtilizationPercentage | int | `80` |  |
| controller.autoscalingTemplate | list | `[]` |  |
| controller.config | object | `{}` | Will add custom configuration options to Nginx https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/ |
| controller.configAnnotations | object | `{}` | Annotations to be added to the controller config configuration configmap. |
| controller.configMapNamespace | string | `""` | Allows customization of the configmap / nginx-configmap namespace; defaults to $(POD_NAMESPACE) |
| controller.containerName | string | `"controller"` | Configures the controller container name |
| controller.containerPort | object | `{"http":80,"https":443}` | Configures the ports that the nginx-controller listens on |
| controller.customTemplate.configMapKey | string | `""` |  |
| controller.customTemplate.configMapName | string | `""` |  |
| controller.defaultSSLCertificate | string | `""` |  |
| controller.disableExternalNameForwarding | bool | `true` | disable-svc-external-name flag |
| controller.dnsConfig | object | `{}` | Optionally customize the pod dnsConfig. |
| controller.dnsPolicy | string | `"ClusterFirst"` | Optionally change this to ClusterFirstWithHostNet in case you have 'hostNetwork: true'. By default, while using host network, name resolution uses the host's DNS. If you wish nginx-controller to keep resolving names inside the k8s network, use ClusterFirstWithHostNet. |
| controller.electionID | string | `""` | Election ID to use for status update, by default it uses the controller name combined with a suffix of 'leader' |
| controller.enableMimalloc | bool | `true` | Enable mimalloc as a drop-in replacement for malloc. # ref: https://github.com/microsoft/mimalloc # |
| controller.enableSSLChainCompletion | bool | `false` |  |
| controller.enableTopologyAwareRouting | bool | `false` | This configuration enables Topology Aware Routing feature, used together with service annotation service.kubernetes.io/topology-aware-hints="auto" Defaults to false |
| controller.existingPsp | string | `""` | Use an existing PSP instead of creating one |
| controller.extraArgs | object | `{}` | Additional command line arguments to pass to nginx-ingress-controller E.g. to specify the default SSL certificate you can use |
| controller.extraContainers | list | `[]` | Additional containers to be added to the controller pod. See https://github.com/lemonldap-ng-controller/lemonldap-ng-controller as example. |
| controller.extraEnvs | list | `[]` | Additional environment variables to set |
| controller.extraInitContainers | list | `[]` | Containers, which are run before the app containers are started. |
| controller.extraModules | list | `[]` | Modules, which are mounted into the core nginx image. See values.yaml for a sample to add opentelemetry module |
| controller.extraVolumeMounts | list | `[]` | Additional volumeMounts to the controller main container. |
| controller.extraVolumes | list | `[]` | Additional volumes to the controller pod. |
| controller.healthCheckHost | string | `""` | Address to bind the health check endpoint. It is better to set this option to the internal node address if the ingress nginx controller is running in the `hostNetwork: true` mode. |
| controller.healthCheckPath | string | `"/healthz"` | Path of the health check endpoint. All requests received on the port defined by the healthz-port parameter are forwarded internally to this path. |
| controller.hostNetwork | bool | `false` | Required for use with CNI based kubernetes installations (such as ones set up by kubeadm), since CNI and hostport don't mix yet. Can be deprecated once https://github.com/kubernetes/kubernetes/issues/23920 is merged |
| controller.hostPort.enabled | bool | `false` | Enable 'hostPort' or not |
| controller.hostPort.ports.http | int | `80` | 'hostPort' http port |
| controller.hostPort.ports.https | int | `443` | 'hostPort' https port |
| controller.hostname | object | `{}` | Optionally customize the pod hostname. |
| controller.image.allowPrivilegeEscalation | bool | `true` |  |
| controller.image.chroot | bool | `false` |  |
| controller.image.digest | string | `""` |  |
| controller.image.digestChroot | string | `""` |  |
| controller.image.image | string | `"giantswarm/ingress-nginx-controller"` |  |
| controller.image.pullPolicy | string | `"IfNotPresent"` |  |
| controller.image.runAsUser | int | `101` |  |
| controller.image.tag | string | `"v1.7.0"` |  |
| controller.ingressClass | string | `"nginx"` | For backwards compatibility with ingress.class annotation, use ingressClass. Algorithm is as follows, first ingressClassName is considered, if not present, controller looks for ingress.class annotation |
| controller.ingressClassByName | bool | `false` | Process IngressClass per name (additionally as per spec.controller). |
| controller.ingressClassResource.controllerValue | string | `"k8s.io/ingress-nginx"` | Controller-value of the controller that is processing this ingressClass |
| controller.ingressClassResource.default | bool | `false` | Is this the default ingressClass for the cluster |
| controller.ingressClassResource.enabled | bool | `true` | Is this ingressClass enabled or not |
| controller.ingressClassResource.name | string | `"nginx"` | Name of the ingressClass |
| controller.ingressClassResource.parameters | object | `{}` | Parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters. |
| controller.keda.apiVersion | string | `"keda.sh/v1alpha1"` |  |
| controller.keda.behavior | object | `{}` |  |
| controller.keda.cooldownPeriod | int | `300` |  |
| controller.keda.enabled | bool | `false` |  |
| controller.keda.maxReplicas | int | `11` |  |
| controller.keda.minReplicas | int | `1` |  |
| controller.keda.pollingInterval | int | `30` |  |
| controller.keda.restoreToOriginalReplicaCount | bool | `false` |  |
| controller.keda.scaledObject.annotations | object | `{}` |  |
| controller.keda.triggers | list | `[]` |  |
| controller.kind | string | `"Deployment"` | Use a `DaemonSet` or `Deployment` |
| controller.labels | object | `{}` | Labels to be added to the controller Deployment or DaemonSet and other resources that do not have option to specify labels # |
| controller.lifecycle | object | `{"preStop":{"exec":{"command":["/wait-shutdown"]}}}` | Improve connection draining when ingress controller pod is deleted using a lifecycle hook: With this new hook, we increased the default terminationGracePeriodSeconds from 30 seconds to 300, allowing the draining of connections up to five minutes. If the active connections end before that, the pod will terminate gracefully at that time. To effectively take advantage of this feature, the Configmap feature worker-shutdown-timeout new value is 240s instead of 10s. # |
| controller.livenessProbe.failureThreshold | int | `5` |  |
| controller.livenessProbe.httpGet.path | string | `"/healthz"` |  |
| controller.livenessProbe.httpGet.port | int | `10254` |  |
| controller.livenessProbe.httpGet.scheme | string | `"HTTP"` |  |
| controller.livenessProbe.initialDelaySeconds | int | `10` |  |
| controller.livenessProbe.periodSeconds | int | `10` |  |
| controller.livenessProbe.successThreshold | int | `1` |  |
| controller.livenessProbe.timeoutSeconds | int | `1` |  |
| controller.maxUnavailable | string | `"25%"` | Define either 'minAvailable' or 'maxUnavailable', never both. |
| controller.maxmindLicenseKey | string | `""` | Maxmind license key to download GeoLite2 Databases. # https://blog.maxmind.com/2019/12/18/significant-changes-to-accessing-and-using-geolite2-databases |
| controller.metrics.enabled | bool | `true` |  |
| controller.metrics.port | int | `10254` |  |
| controller.metrics.portName | string | `"metrics"` |  |
| controller.metrics.prometheusRule.additionalLabels | object | `{}` |  |
| controller.metrics.prometheusRule.enabled | bool | `false` |  |
| controller.metrics.prometheusRule.rules | list | `[]` |  |
| controller.metrics.service.annotations | object | `{}` |  |
| controller.metrics.service.externalIPs | list | `[]` | List of IP addresses at which the stats-exporter service is available # Ref: https://kubernetes.io/docs/user-guide/services/#external-ips # |
| controller.metrics.service.labels | object | `{}` | Labels to be added to the metrics service resource |
| controller.metrics.service.loadBalancerSourceRanges | list | `[]` |  |
| controller.metrics.service.servicePort | int | `10254` |  |
| controller.metrics.service.type | string | `"ClusterIP"` |  |
| controller.metrics.serviceMonitor.additionalLabels | object | `{}` |  |
| controller.metrics.serviceMonitor.enabled | bool | `false` |  |
| controller.metrics.serviceMonitor.metricRelabelings | list | `[]` |  |
| controller.metrics.serviceMonitor.namespace | string | `""` |  |
| controller.metrics.serviceMonitor.namespaceSelector | object | `{}` |  |
| controller.metrics.serviceMonitor.relabelings | list | `[]` |  |
| controller.metrics.serviceMonitor.scrapeInterval | string | `"30s"` |  |
| controller.metrics.serviceMonitor.targetLabels | list | `[]` |  |
| controller.minReadySeconds | int | `0` | `minReadySeconds` to avoid killing pods before we are ready # |
| controller.name | string | `"controller"` |  |
| controller.networkPolicy.enabled | bool | `true` | Enable 'networkPolicy' or not |
| controller.nodeSelector | object | `{"kubernetes.io/os":"linux"}` | Node labels for controller pod assignment # Ref: https://kubernetes.io/docs/user-guide/node-selection/ # |
| controller.opentelemetry.containerSecurityContext.allowPrivilegeEscalation | bool | `false` |  |
| controller.opentelemetry.enabled | bool | `false` |  |
| controller.opentelemetry.image | string | `"registry.k8s.io/ingress-nginx/opentelemetry:v20230312-helm-chart-4.5.2-28-g66a760794@sha256:40f766ac4a9832f36f217bb0e98d44c8d38faeccbfe861fbc1a76af7e9ab257f"` |  |
| controller.podAnnotations | object | `{}` | Annotations to be added to controller pods # |
| controller.podLabels | object | `{}` | Labels to add to the pod container metadata |
| controller.podSecurityContext | object | `{}` | Security Context policies for controller pods |
| controller.priorityClassName | string | `""` |  |
| controller.proxySetHeaders | object | `{}` | Will add custom headers before sending traffic to backends according to https://github.com/kubernetes/ingress-nginx/tree/main/docs/examples/customization/custom-headers |
| controller.publishService | object | `{"enabled":true,"pathOverride":""}` | Allows customization of the source of the IP address or FQDN to report in the ingress status field. By default, it reads the information provided by the service. If disable, the status field reports the IP address of the node or nodes where an ingress controller pod is running. |
| controller.publishService.enabled | bool | `true` | Enable 'publishService' or not |
| controller.publishService.pathOverride | string | `""` | Allows overriding of the publish service to bind to Must be <namespace>/<service_name> |
| controller.readinessProbe.failureThreshold | int | `3` |  |
| controller.readinessProbe.httpGet.path | string | `"/healthz"` |  |
| controller.readinessProbe.httpGet.port | int | `10254` |  |
| controller.readinessProbe.httpGet.scheme | string | `"HTTP"` |  |
| controller.readinessProbe.initialDelaySeconds | int | `10` |  |
| controller.readinessProbe.periodSeconds | int | `10` |  |
| controller.readinessProbe.successThreshold | int | `1` |  |
| controller.readinessProbe.timeoutSeconds | int | `1` |  |
| controller.replicaCount | int | `2` |  |
| controller.reportNodeInternalIp | bool | `false` | Bare-metal considerations via the host network https://kubernetes.github.io/ingress-nginx/deploy/baremetal/#via-the-host-network Ingress status was blank because there is no Service exposing the NGINX Ingress controller in a configuration using the host network, the default --publish-service flag used in standard cloud setups does not apply |
| controller.resources.requests.cpu | string | `"500m"` |  |
| controller.resources.requests.memory | string | `"600Mi"` |  |
| controller.scope.enabled | bool | `false` | Enable 'scope' or not |
| controller.scope.namespace | string | `""` | Namespace to limit the controller to; defaults to $(POD_NAMESPACE) |
| controller.scope.namespaceSelector | string | `""` | When scope.enabled == false, instead of watching all namespaces, we watching namespaces whose labels only match with namespaceSelector. Format like foo=bar. Defaults to empty, means watching all namespaces. |
| controller.service.annotations | object | `{}` |  |
| controller.service.appProtocol | bool | `true` | If enabled is adding an appProtocol option for Kubernetes service. An appProtocol field replacing annotations that were using for setting a backend protocol. Here is an example for AWS: service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http It allows choosing the protocol for each backend specified in the Kubernetes service. See the following GitHub issue for more details about the purpose: https://github.com/kubernetes/kubernetes/issues/40244 Will be ignored for Kubernetes versions older than 1.20 # |
| controller.service.enableHttp | bool | `true` |  |
| controller.service.enableHttps | bool | `true` |  |
| controller.service.enabled | bool | `true` |  |
| controller.service.external.enabled | bool | `true` |  |
| controller.service.externalDNS.annotation | string | `"giantswarm.io/external-dns: managed"` |  |
| controller.service.externalDNS.enabled | bool | `true` |  |
| controller.service.externalIPs | list | `[]` | List of IP addresses at which the controller services are available # Ref: https://kubernetes.io/docs/user-guide/services/#external-ips # |
| controller.service.externalTrafficPolicy | string | `"Local"` |  |
| controller.service.internal.annotations | object | `{}` | Annotations are mandatory for the load balancer to come up. Varies with the cloud service. |
| controller.service.internal.enabled | bool | `false` | Enables an additional internal load balancer (besides the external one). |
| controller.service.internal.externalTrafficPolicy | string | `"Local"` |  |
| controller.service.internal.loadBalancerSourceRanges | list | `[]` | Restrict access For LoadBalancer service. Defaults to 0.0.0.0/0. |
| controller.service.internal.nodePorts.http | int | `30012` |  |
| controller.service.internal.nodePorts.https | int | `30013` |  |
| controller.service.internal.nodePorts.tcp | object | `{}` |  |
| controller.service.internal.nodePorts.udp | object | `{}` |  |
| controller.service.internal.subdomain | string | `"ingress-internal"` |  |
| controller.service.internal.suffix | string | `""` |  |
| controller.service.ipFamilies | list | `["IPv4"]` | List of IP families (e.g. IPv4, IPv6) assigned to the service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. # Ref: https://kubernetes.io/docs/concepts/services-networking/dual-stack/ |
| controller.service.ipFamilyPolicy | string | `"SingleStack"` | Represents the dual-stack-ness requested or required by this Service. Possible values are SingleStack, PreferDualStack or RequireDualStack. The ipFamilies and clusterIPs fields depend on the value of this field. # Ref: https://kubernetes.io/docs/concepts/services-networking/dual-stack/ |
| controller.service.labels | object | `{}` |  |
| controller.service.loadBalancerIP | string | `""` | Used by cloud providers to connect the resulting `LoadBalancer` to a pre-existing static IP according to https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer |
| controller.service.loadBalancerSourceRanges | list | `[]` |  |
| controller.service.nodePorts.http | int | `30010` |  |
| controller.service.nodePorts.https | int | `30011` |  |
| controller.service.nodePorts.tcp | object | `{}` |  |
| controller.service.nodePorts.udp | object | `{}` |  |
| controller.service.ports.http | int | `80` |  |
| controller.service.ports.https | int | `443` |  |
| controller.service.public | bool | `true` |  |
| controller.service.subdomain | string | `"ingress"` |  |
| controller.service.suffix | string | `""` |  |
| controller.service.targetPorts.http | string | `"http"` |  |
| controller.service.targetPorts.https | string | `"https"` |  |
| controller.service.type | string | `"LoadBalancer"` |  |
| controller.shareProcessNamespace | bool | `false` |  |
| controller.sysctls | object | `{}` | See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for notes on enabling and using sysctls |
| controller.tcp.annotations | object | `{}` | Annotations to be added to the tcp config configmap |
| controller.tcp.configMapNamespace | string | `""` | Allows customization of the tcp-services-configmap; defaults to $(POD_NAMESPACE) |
| controller.terminationGracePeriodSeconds | int | `300` | `terminationGracePeriodSeconds` to avoid killing pods before we are ready # wait up to five minutes for the drain of connections # |
| controller.tolerations | list | `[]` | Node tolerations for server scheduling to nodes with taints # Ref: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ # |
| controller.topologySpreadConstraints | string | `"- labelSelector:\n    matchLabels:\n      {{- include \"ingress-nginx.selectorLabels\" . | nindent 6 }}\n      app.kubernetes.io/component: controller\n  topologyKey: topology.kubernetes.io/zone\n  maxSkew: 1\n  whenUnsatisfiable: ScheduleAnyway\n- labelSelector:\n    matchLabels:\n      {{- include \"ingress-nginx.selectorLabels\" . | nindent 6 }}\n      app.kubernetes.io/component: controller\n  topologyKey: kubernetes.io/hostname\n  maxSkew: 1\n  whenUnsatisfiable: ScheduleAnyway"` | Topology spread constraints rely on node labels to identify the topology domain(s) that each Node is in. # Ref: https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/ # |
| controller.udp.annotations | object | `{}` | Annotations to be added to the udp config configmap |
| controller.udp.configMapNamespace | string | `""` | Allows customization of the udp-services-configmap; defaults to $(POD_NAMESPACE) |
| controller.updateIngressStatus | bool | `true` |  |
| controller.updateStrategy | object | `{}` | The update strategy to apply to the Deployment or DaemonSet # |
| controller.watchIngressWithoutClass | bool | `false` | Process Ingress objects without ingressClass annotation/ingressClassName field Overrides value for --watch-ingress-without-class flag of the controller binary Defaults to false |
| defaultBackend.affinity | object | `{}` |  |
| defaultBackend.autoscaling.annotations | object | `{}` |  |
| defaultBackend.autoscaling.enabled | bool | `false` |  |
| defaultBackend.autoscaling.maxReplicas | int | `2` |  |
| defaultBackend.autoscaling.minReplicas | int | `1` |  |
| defaultBackend.autoscaling.targetCPUUtilizationPercentage | int | `50` |  |
| defaultBackend.autoscaling.targetMemoryUtilizationPercentage | int | `50` |  |
| defaultBackend.containerSecurityContext | object | `{}` | Security Context policies for controller main container. See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for notes on enabling and using sysctls # |
| defaultBackend.enabled | bool | `false` |  |
| defaultBackend.existingPsp | string | `""` | Use an existing PSP instead of creating one |
| defaultBackend.extraArgs | object | `{}` |  |
| defaultBackend.extraEnvs | list | `[]` | Additional environment variables to set for defaultBackend pods |
| defaultBackend.extraVolumeMounts | list | `[]` |  |
| defaultBackend.extraVolumes | list | `[]` |  |
| defaultBackend.image.allowPrivilegeEscalation | bool | `false` |  |
| defaultBackend.image.image | string | `"giantswarm/defaultbackend"` |  |
| defaultBackend.image.pullPolicy | string | `"IfNotPresent"` |  |
| defaultBackend.image.readOnlyRootFilesystem | bool | `true` |  |
| defaultBackend.image.runAsNonRoot | bool | `true` |  |
| defaultBackend.image.runAsUser | int | `65534` |  |
| defaultBackend.image.tag | string | `"1.5"` |  |
| defaultBackend.labels | object | `{}` | Labels to be added to the default backend resources |
| defaultBackend.livenessProbe.failureThreshold | int | `3` |  |
| defaultBackend.livenessProbe.initialDelaySeconds | int | `30` |  |
| defaultBackend.livenessProbe.periodSeconds | int | `10` |  |
| defaultBackend.livenessProbe.successThreshold | int | `1` |  |
| defaultBackend.livenessProbe.timeoutSeconds | int | `5` |  |
| defaultBackend.minAvailable | int | `1` |  |
| defaultBackend.minReadySeconds | int | `0` | `minReadySeconds` to avoid killing pods before we are ready # |
| defaultBackend.name | string | `"defaultbackend"` |  |
| defaultBackend.networkPolicy.enabled | bool | `true` | Enable 'networkPolicy' or not |
| defaultBackend.nodeSelector | object | `{"kubernetes.io/os":"linux"}` | Node labels for default backend pod assignment # Ref: https://kubernetes.io/docs/user-guide/node-selection/ # |
| defaultBackend.podAnnotations | object | `{}` | Annotations to be added to default backend pods # |
| defaultBackend.podLabels | object | `{}` | Labels to add to the pod container metadata |
| defaultBackend.podSecurityContext | object | `{}` | Security Context policies for controller pods See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for notes on enabling and using sysctls # |
| defaultBackend.port | int | `8080` |  |
| defaultBackend.priorityClassName | string | `""` |  |
| defaultBackend.readinessProbe.failureThreshold | int | `6` |  |
| defaultBackend.readinessProbe.initialDelaySeconds | int | `0` |  |
| defaultBackend.readinessProbe.periodSeconds | int | `5` |  |
| defaultBackend.readinessProbe.successThreshold | int | `1` |  |
| defaultBackend.readinessProbe.timeoutSeconds | int | `5` |  |
| defaultBackend.replicaCount | int | `1` |  |
| defaultBackend.resources | object | `{}` |  |
| defaultBackend.service.annotations | object | `{}` |  |
| defaultBackend.service.externalIPs | list | `[]` | List of IP addresses at which the default backend service is available # Ref: https://kubernetes.io/docs/user-guide/services/#external-ips # |
| defaultBackend.service.loadBalancerSourceRanges | list | `[]` |  |
| defaultBackend.service.servicePort | int | `80` |  |
| defaultBackend.service.type | string | `"ClusterIP"` |  |
| defaultBackend.serviceAccount.automountServiceAccountToken | bool | `true` |  |
| defaultBackend.serviceAccount.create | bool | `true` |  |
| defaultBackend.serviceAccount.name | string | `""` |  |
| defaultBackend.tolerations | list | `[]` | Node tolerations for server scheduling to nodes with taints # Ref: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ # |
| defaultBackend.updateStrategy | object | `{}` | The update strategy to apply to the Deployment or DaemonSet # |
| dhParam | string | `""` | A base64-encoded Diffie-Hellman parameter. This can be generated with: `openssl dhparam 4096 2> /dev/null | base64` # Ref: https://github.com/kubernetes/ingress-nginx/tree/main/docs/examples/customization/ssl-dh-param |
| image.registry | string | `"quay.io"` |  |
| imagePullSecrets | list | `[]` | Optional array of imagePullSecrets containing private registry credentials # Ref: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/ |
| podSecurityPolicy.enabled | bool | `true` |  |
| portNamePrefix | string | `""` | Prefix for TCP and UDP ports names in ingress controller service # Some cloud providers, like Yandex Cloud may have a requirements for a port name regex to support cloud load balancer integration |
| provider | string | `"aws"` |  |
| rbac.create | bool | `true` |  |
| rbac.scope | bool | `false` |  |
| revisionHistoryLimit | int | `10` | Rollback limit # |
| serviceAccount.annotations | object | `{}` | Annotations for the controller service account |
| serviceAccount.automountServiceAccountToken | bool | `true` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `""` |  |
| tcp | object | `{}` | TCP service key-value pairs # Ref: https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/exposing-tcp-udp-services.md # |
| udp | object | `{}` | UDP service key-value pairs # Ref: https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/exposing-tcp-udp-services.md # |
