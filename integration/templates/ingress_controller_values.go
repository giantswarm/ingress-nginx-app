// +build k8srequired

package templates

// IngressControllerValues defines value overrides to use in e2e test.
const IngressControllerValues = `controller:
  resources:
    requests:
      cpu: 500m
      memory: 600Mi
  service:
    enabled: true
`
