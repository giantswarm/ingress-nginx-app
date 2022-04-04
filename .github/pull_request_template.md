<!--
@team-cabbage will be automatically requested for review once
this PR has been submitted.
-->

### Tests on workload clusters (not always required)

For changes in the chart, chart templates, and ingress controller container images, I executed the following tests
to verify them working in live enviromnents:

| Test / Provider | AWS | Azure | KVM |
| --- | --- | --- | --- |
| Upgrade from previous version |  |  |  |
| Existing Ingress resources are reconciled correctly |  |  |  |
| Fresh install |  |  |  |
| Fresh Ingress resources are reconciled correctly |  |  |  |

Testing was done using `hello-world-app`.

Hint for KVM:

```
kubectl port-forward -n kube-system svc/nginx-ingress-controller-app 8080:80
ingress_domain=host.configured.in.ingress; curl --connect-to "$ingress_domain:80:127.0.0.1:8080" "http://$ingress_domain" -v
```
