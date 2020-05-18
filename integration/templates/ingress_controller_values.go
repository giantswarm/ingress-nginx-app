// +build k8srequired

package templates

// IngressControllerValues defines value overrides to use in e2e test.
const IngressControllerValues = `cluster:
  profile: 3
controller:
  autoscaling:
    enabled: false
  replicaCount: 2
`
