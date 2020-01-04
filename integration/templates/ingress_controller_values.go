// +build k8srequired

package templates

// IngressControllerValues sets legacy to true so the controller service uses
// node ports.
const IngressControllerValues = `ingressController:
  legacy: true
`
