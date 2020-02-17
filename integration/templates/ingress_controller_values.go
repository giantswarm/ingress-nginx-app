// +build k8srequired

package templates

// IngressControllerValues defines value overrides to use in e2e test.
const IngressControllerValues = `controller:
  service:
    enabled: true
`
