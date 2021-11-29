<!--
@team-cabbage will be automatically requested for review once
this PR has been submitted.
-->

### Tests on workload clusters (not always required)

In order to verify that my changes also work on, I did the following tests:

#### AWS

- [ ] Upgrade from previous version works
- [ ] Existing Ingress resources are reconciled correctly (change domain, see if its available)
- [ ] Fresh install works
- [ ] Fresh Ingress resources are reconciled correctly

#### Azure

- [ ] Upgrade from previous version works
- [ ] Existing Ingress resources are reconciled correctly (change domain, see if its available)
- [ ] Fresh install works
- [ ] Fresh Ingress resources are reconciled correctly

#### KVM

Hint:

```
kubectl port-forward -n kube-system svc/nginx-ingress-controller-app 8080:80
curl -H "Host: host.configured.in.ingress" localhost:8080
```

- [ ] Upgrade from previous version works
- [ ] Existing Ingress resources are reconciled correctly (change domain, see if its available)
- [ ] Fresh install works
- [ ] Fresh Ingress resources are reconciled correctly
