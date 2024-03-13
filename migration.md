# Migration from `nginx-ingress-controller-app`

Unfortunately it is not possible to migrate from the old `nginx-ingress-controller-app` chart to this one just by bumping the version. This happens due to several breaking changes, e.g. the change of selector labels in the `Deployment` resource.

To still be able to upgrade to this chart without major outages (minor service disruptions can not be prevented due to pods being restarted like in a normal update or change scenario), we developed a step-by-step guide which replaces your old app deployment.

This guide takes care of several extended deployment scenarios like ExternalDNS reconciling both your Ingress NGINX Controller `Service` resource's hostname and those defined in your `Ingress` resources or having multiple Ingress NGINX Controllers installed in your cluster.

In general there are three steps, each of them changing a single configuration value and slowly handing over responsibilities to the new Ingress NGINX Controller deployment.

Please read the following steps thoroughly and reach out to our support if you are having any questions or are not feeling confident with doing this change on your own. We highly recommend to first try this procedure in a non-production environment as similar to your production environment as possible.

## Caveats

### Configuration management tools

If you are using Flux or any comparable solution to apply and reconcile configurations to your cluster, we recommend suspending it for the duration of this maintenance and update the according configuration source before resuming it. You can still implement all of the following changes using your tooling step by step, but you should thorougly test this in a non-production environment and suspend ExternalDNS in the second step since this is a time critical part in the whole procedure.

### ValidatingWebhookConfiguration

During the upgrade, two Ingress NGINX Controller instances will coexist, each deploying a `ValidatingWebhookConfiguration` with identical rules targeting the same `apiGroups`. Consequently, a request must pass both sets of validations to proceed. For example, difficulties arose when enabling the `OpenTelemetry` plugin on the new instance, requiring extra configuration and module loading, leading to validation failures that prevented the new instance from starting.
To prevent conflicts, it's advisable to postpone any new configurations until the upgrade completes and the previous instance is removed. If retaining the old instance is necessary, disabling its `ValidatingWebhookConfiguration` is recommended to prevent validation issues:

```
controller:
  admissionWebhooks:
    enabled: false
```

## Legacy KVM product

This section only applies to our legacy KVM product. Please skip if you are running on any other platform.

The old `nginx-ingress-controller-app` chart ships with some changes to the upstream's default values. Out of the box it uses pre-defined node ports when deployed with a `Service` resource of type `NodePort`. This is required due to a pre-created `Service` resource of type `NodePort` in your management cluster pointing to those pre-defined node ports and forwarding traffic from the outside to your workload cluster.

For the same reason you can not deploy the new `ingress-nginx` chart side-by-side with the old `nginx-ingress-controller-app` one and then slowly hand over traffic as described below, as this would end up in a port collision. So unfortunately you will have to first completely remove the old `nginx-ingress-controller-app` deployment and then deploy the new `ingress-nginx` chart afterwards. Since the latter is dropping the before mentioned pre-defined node ports, you will also have to configure them in the values on your own:

```yaml
controller:
  service:
    nodePorts:
      http: 30010
      https: 30011
    internal:
      nodePorts:
        http: 30012
        https: 30013
```

The other steps described in this document do not apply to you, so you are already done migrating to the new `ingress-nginx` chart here.

Optionally you can still stick to the latest `v2.*.*` release of the `nginx-ingress-controller-app` chart. We will continue implementing patches and relevant features there while you are migrating your environment to our new on-premise product(s).

## Step 0: Initial setup

For this procedure to work out, we assume you are currently running `nginx-ingress-controller-app` with some essential configuration parameters either set as follows or left untouched, so their default is being used:

```yaml
controller:
  ingressClassResource:
    enabled: true
  service:
    externalDNS:
      enabled: true
  updateIngressStatus: true
```

`controller.ingressClassResource.enabled` is `true` by default and ensures your `nginx-ingress-controller-app` deployment creates the required `IngressClass` resource. If you disabled this and manage your `IngressClass` resource(s) on your own, feel free to skip the according step, but also make sure to keep this setting disabled in the new `ingress-nginx` deployment.

`controller.service.externalDNS.enabled` is also `true` by default and tells our chart to add a `hostname` annotation to the `Service` resource which then can be reconciled by an instance of ExternalDNS. If you are not using this feature, aka not referencing any services published through your Ingress NGINX Controller by using the `Service` resource's hostname, you can safely skip the according step. Again also make sure to keep this setting disabled in the new `ingress-nginx` deployment.

Last but not least and probably the most important, there is `controller.updateIngressStatus`. While this is still a separate configuration value in the `nginx-ingress-controller-app` chart, it got removed in favor of setting `controller.extraArgs.update-status` in the `ingress-nginx` chart. This value is set to `true` by default and so tells the Ingress NGINX Controller pods to update all `Ingress` resources assigned to them with the address of the `Service` resource the Ingress NGINX Controller is being published with. This is especially important for ExternalDNS creating and reconciling DNS records for those `Ingress` resources. So the moment we hand over this responsibility to the new `ingress-nginx` deployment, its pods will change the status of all `Ingress` resources assigned to them. Afterwards ExternalDNS can update the DNS records for those `Ingress` resources.

This is why this value is being changed at last. It also inflicts a restart of the according pods. To prevent multiple Ingress NGINX Controller deployments from updating the status of the same `Ingress` resources, we first disable this feature for the old deployment and then enable it for the new one. This also means there will be a short period in time where no Ingress NGINX Controller is acutally updating the status of all `Ingress` resources assigned to them. Any changes to those `Ingress` resources, either creating new ones or updating/deleting existing ones, will still be reconciled by both Ingress NGINX Controllers but none of them will actually update their status, which results in the implementing load balancer address staying the same and therefore not chaning any DNS records through instances of ExternalDNS.

As soon as the new Ingress NGINX Controller deployment is up and running with `controller.extraArgs.update-status` set to `"true"`, its pods will automatically update the status of all `Ingress` resources assigned to them to the address of the new `Service` resource.

Before kicking off this procedure, you should already have installed a release of the `ingress-nginx` chart to your cluster. You can continue using the values of for your old `nginx-ingress-controller-app` deployment, but please make sure to check the [`CHANGELOG.md`](https://github.com/giantswarm/ingress-nginx-app/blob/main/CHANGELOG.md) for relevant changes to them. Additionally make sure to set the following values:

```yaml
controller:
  ingressClassResource:
    enabled: false
  service:
    externalDNS:
      enabled: false
  extraArgs:
    update-status: "false"
```

As mentioned before, those values will change during the migration procedure. If you disabled some of them in your old `nginx-ingress-controller-app` deployment on purpose, please feel free to keep them disabled in the according steps.

Please make sure the new `ingress-nginx` deployment is up and running before proceeding to the next step.

## Step 1: Handing over the `IngressClass` resource

If you decided not to use the default `IngressClass` shipped with any of the Ingress NGINX Controller charts and therefore already disabled `controller.ingressClassResource.enabled` beforehand, it is safe to skip this step. Just make sure to also keep this value disabled in your new `ingress-nginx` deployment.

By default both charts, the old `nginx-ingress-controller-app` and the new `ingress-nginx` one, deploy an `IngressClass` resource called `nginx`. Depending on your current environment and particular deployment option, this name can differ. Regardless of its name, an `IngressClass` resource is immutable and therefore can not be changed after creation. Additionally Helm adds annotations to resources so it can tell which release is managing which resources and which release is actually allowed to change them.

This is why we first need to make sure the old `nginx-ingress-controller-app` is no longer managing nor creating this default `IngressClass` resource by disabling `controller.ingressClassResource.enabled`. To do so, one can use the following values for the old `nginx-ingress-controller-app` deployment:

```yaml
controller:
  ingressClassResource:
    enabled: false
  service:
    externalDNS:
      enabled: true
  updateIngressStatus: true
```

After updating the values, the default `IngressClass` resource should be gone. You can check this by running the following command (`IngressClass` resources are not namespaced, so no `--namespace` flag needed):

```bash
kubectl get ingressclasses
```

**Note:** Your existing Ingress NGINX Controller pods will not crash without an `IngressClass` resource, but they probably will not reconcile changes to `Ingress` resources. Additionally new Ingress NGINX Controller pods might fail to come up without their `IngressClass` resource. To reduce the risk of a service outage, we recommend to proceed on this step as fast as possible.

As soon as the `IngressClass` resource managed by your old `nginx-ingress-controller-app` deployment has gone, you can safely go ahead and let the new `ingress-nginx` deployment re-create it by applying the following values to it:

```yaml
controller:
  ingressClassResource:
    enabled: true
  service:
    externalDNS:
      enabled: false
  extraArgs:
    update-status: "false"
```

Run the above `kubectl` command again to ensure the `IngressClass` resource has been re-created. As soon as the new `IngressClass` resource has been created, you can proceed to the next step.

## Step 2: Handing over the `Service` resource's hostname

This step is only required if you chose to let an ExternalDNS instance reconcile a DNS record for your Ingress NGINX Controller's `Service` resource. By default this DNS record is called something like `ingress.<base-domain>`, so for example `ingress.cluster.k8s.installation.region.provider.gigantic.io`. For ease of use it is possible to create `CNAME` records pointing to this `A` record to make your services accessible. In case you are doing so, those `CNAME` records' target address will be automatically updated in this step.

We will first configure the new `ingress-nginx` deployment to add this `hostname` annotation to its `Service` resource and then remove it from the old `nginx-ingress-controller-app` afterwards. This way a possible reconcilation loop of ExternalDNS at best only updates the record's value to the new `Service` resource's address. Even though we tested this on AWS multiple times, we strongly recommend to turn off (scale down) any ExternalDNS instance reconciling this record for the duration of this step and turn it back on afterwards. This way the DNS record gets updated once any required changes to your `Service` resource have been executed and checked by you.

As mentioned above we will first configure the new `ingress-nginx` deployment to add the `hostname` annotation to its `Service` resource. This can be achieved by applying the follow values to the `ingress-nginx` deployment:

```yaml
controller:
  ingressClassResource:
    enabled: true
  service:
    externalDNS:
      enabled: true
  extraArgs:
    update-status: "false"
```

You can check the existence of the required annotations by executing the following command:

```
kubectl get service --namespace <namespace> <service> --output yaml
```

Please replace `namespace` by the namespace you installed the new `ingress-nginx` deployment to and `service` by the name of the `Service` resource. If you chose `ingress-nginx` as the app's name, this will be `ingress-nginx-controller`, or something like `<app-name>-ingress-nginx-controller` otherwise.

The resulting output should look like this:

```yaml
apiVersion: v1
kind: Service
metadata:
  [...]
  annotations:
    external-dns.alpha.kubernetes.io/hostname: ingress.cluster.k8s.installation.region.provider.gigantic.io
    giantswarm.io/external-dns: managed
  [...]
```

As soon as your `Service` resource contains the mentioned annotations, you can go ahead and remove the same from the old `nginx-ingress-controller-app` deployment by applying the following values:

```yaml
controller:
  ingressClassResource:
    enabled: false
  service:
    externalDNS:
      enabled: false
  updateIngressStatus: true
```

Repeat the `kubectl` command from above for the namespace and name of your old `nginx-ingress-controller-app` deployment to verify the `hostname` annotation has been removed. If everything looks fine, you can safely turn back on your ExternalDNS instance. Check its logs after it comes up to see if it successfully updated the DNS record of your Ingress NGINX Controller `Service` resource.

Starting from here, every service published by referencing this DNS record should shortly be handed over to the new `ingress-nginx` deployment. Depending on the TTL configured for the record, it can take some time until all your clients and DNS resolvers around the world recognize the new address. Client requests should slowly start hitting the new pods now. See the logs of your `ingress-nginx` pods and maybe check the functionality of the new Ingress NGINX Controller deployment before heading to the last step.

## Step 3: Handing over the `Ingress` resources

In this last step we will finally tell your old `nginx-ingress-controller-app` pods to no longer update the status of the `Ingress` resources assigned to them and instead let the pods of your new `ingress-nginx` deployment do so. If you already disabled this feature in your `nginx-ingress-controller-app` deployment, maybe because you are running multiple Ingress NGINX Controllers reconciling the same `Ingress` resources, you can safely skip this step. Just also make sure to keep this setting disabled in the new `ingress-nginx` deployment by setting `controller.extraArgs.update-status` to `"false"`.

Due to `--update-status` being a flag passed to the container directly, this step results in a change of the pod template and therefore inflicts a restart of the affected Ingress NGINX Controller pods. Depending on your environment and especially if you are using `externalTrafficPolicy: Local` in your `Service` resource, this might cause a minor service disruption due to the cloud provider's load balancer taking some time until realizing a node of its target group is no longer eligible for traffic.

To mitigate this issue, one can set `controller.service.externalTrafficPolicy` and/or `controller.service.internal.externalTrafficPolicy` to `Cluster` for the duration of this step, so all nodes of your cluster are getting eligible for receiving and distributing traffic internally instead of only those running at least one pod of an Ingress NGINX Controller. Keep in mind that this might also impact source IP preservation.

Since two Ingress NGINX Controllers trying to update the status of the same `Ingress` resources results in a clash, we will first disable this feature in your old `nginx-ingress-controller-app` deployment and enable it in the new `ingress-nginx` deployment afterwards.

To do so, first update the old `nginx-ingress-controller-app` with the following values:

```yaml
controller:
  ingressClassResource:
    enabled: false
  service:
    externalDNS:
      enabled: false
  updateIngressStatus: false
```

The pods of the affected Ingress NGINX Controller deployment will now restart and new pods will no longer update the status of `Ingress` resources assigned to them. As mentioned before, this means the address of your `Service` resource will not be propagated to new or updated in existing `Ingress` resources and therefore ExternalDNS will not reconcile DNS records for them.

After you ensured all of the pods of the old `nginx-ingress-controller-app` deployment have been restarted and are up & running again, you can proceed to update the values of your new `ingress-nginx` deployment:

```yaml
controller:
  ingressClassResource:
    enabled: true
  service:
    externalDNS:
      enabled: true
  extraArgs:
    update-status: "true"
```

Please note the actual configuration value is no longer called `controller.updateIngressStatus` but `controller.extraArgs.update-status` and needs to be a string instead of a boolean.

After changing this value in your `ingress-nginx` deployment, its pods will be restarted, too, and then start to update the status of the `Ingress` resources assigned to them to the new `Service` resource's address. ExternalDNS will then automatically update the related DNS records and clients will start to access your services via the new Ingress NGINX Controller.

As soon as this happens, you can check both the logs of your old `nginx-ingress-controller-app` deployment and the new `ingress-nginx` deployment. Please check remaining and maybe manually set DNS records if the former is still receiving requests. You can keep the old Ingress NGINX Controller running for a while, double check it is not receiving any requests anymore and then safely remove it from your cluster.
