package basic

import (
	"context"
	"fmt"
	"time"

	// "io"
	"net"
	"net/http"
	"net/url"
	"os"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"github.com/giantswarm/apiextensions-application/api/v1alpha1"
	"github.com/giantswarm/apptest-framework/pkg/state"
	"github.com/giantswarm/clustertest/pkg/application"
	"github.com/giantswarm/clustertest/pkg/logger"
	"github.com/giantswarm/clustertest/pkg/wait"

	networkingv1 "k8s.io/api/networking/v1"
	"k8s.io/apimachinery/pkg/types"
	ctrl "sigs.k8s.io/controller-runtime/pkg/client"
)

func getHelloWorldApp(ingressHost string) (*application.Application, error) {
	org := state.GetCluster().Organization
	helloWorldAppValues := map[string]string{"IngressHost": ingressHost}
	helloWorldApp := application.New(fmt.Sprintf("%s-hello-world", state.GetCluster().Name), "hello-world").
		WithCatalog("giantswarm").
		WithOrganization(*org).
		WithVersion("latest").
		WithClusterName(state.GetCluster().Name).
		WithInCluster(false).
		WithInstallNamespace("default").
		MustWithValuesFile("./test_data/helloworld_values.yaml", &application.TemplateValues{
			ClusterName:  state.GetCluster().Name,
			Organization: state.GetCluster().Organization.Name,
			ExtraValues:  helloWorldAppValues,
		})

	err := state.GetFramework().MC().DeployApp(state.GetContext(), *helloWorldApp)
	return helloWorldApp, err
}

func ingressHasLB(ingressNamespace, ingressName string) (bool, error) {

	wcClient, err := state.GetFramework().WC(state.GetCluster().Name)
	if err != nil {
		return false, err
	}

	logger.Log("Checking if ingress has load balancer set in status")
	ingress := networkingv1.Ingress{}
	err = wcClient.Get(state.GetContext(), types.NamespacedName{Name: ingressName, Namespace: ingressNamespace}, &ingress)
	if err != nil {
		logger.Log("Failed to get ingress: %v", err)
		return false, err
	}

	if ingress.Status.LoadBalancer.Ingress != nil &&
		len(ingress.Status.LoadBalancer.Ingress) > 0 &&
		ingress.Status.LoadBalancer.Ingress[0].Hostname != "" {

		logger.Log("Load balancer hostname found in ingress status: %s", ingress.Status.LoadBalancer.Ingress[0].Hostname)
		return true, nil
	}

	return false, nil
}

func getHttpClientWithProxy() *http.Client {
	transport := &http.Transport{
		DialContext: func(ctx context.Context, network, addr string) (net.Conn, error) {
			dialer := &net.Dialer{
				Resolver: &net.Resolver{
					PreferGo: true,
					Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
						if os.Getenv("HTTP_PROXY") != "" {
							u, err := url.Parse(os.Getenv("HTTP_PROXY"))
							if err != nil {
								logger.Log("Error parsing HTTP_PROXY as a URL %s", os.Getenv("HTTP_PROXY"))
							} else {
								if addr == u.Host {
									// always use coredns for proxy address resolution.
									var d net.Dialer
									return d.Dial(network, address)
								}
							}
						}
						d := net.Dialer{
							Timeout: time.Millisecond * time.Duration(10000),
						}
						return d.DialContext(ctx, "udp", "8.8.4.4:53")
					},
				},
			}
			return dialer.DialContext(ctx, network, addr)
		},
	}

	if os.Getenv("HTTP_PROXY") != "" {
		logger.Log("Detected need to use PROXY as HTTP_PROXY env var was set to %s", os.Getenv("HTTP_PROXY"))
		transport.Proxy = http.ProxyFromEnvironment
	}

	httpClient := &http.Client{
		Transport: transport,
	}
	return httpClient
}

func getWorkloadClusterBaseDomain() string {
	values := &application.DefaultAppsValues{}
	err := state.GetFramework().MC().GetHelmValues(state.GetCluster().Name, state.GetCluster().GetNamespace(), values)
	Expect(err).NotTo(HaveOccurred())

	if values.BaseDomain == "" {
		Fail("baseDomain field missing from cluster helm values")
	}

	return fmt.Sprintf("%s.%s", state.GetCluster().Name, values.BaseDomain)
}

func waitWithPatch(app *application.Application) (bool, error) {
	// We keep patching the `App` CR by adding a label. This way, we trigger reconciliation loops in chart-operator.
	mcKubeClient := state.GetFramework().MC()

	application := &v1alpha1.App{}
	err := mcKubeClient.Get(state.GetContext(), types.NamespacedName{Name: app.InstallName, Namespace: app.GetNamespace()}, application)
	if err != nil {
		return false, err
	}

	now := time.Now()
	patchedApp := application.DeepCopy()
	labels := patchedApp.GetLabels()
	labels["update"] = fmt.Sprintf("%d", now.Unix())
	patchedApp.SetLabels(labels)

	err = mcKubeClient.Patch(state.GetContext(), patchedApp, ctrl.MergeFrom(application))
	if err != nil {
		return false, err
	}

	return wait.IsAppDeployed(state.GetContext(), state.GetFramework().MC(), app.InstallName, app.GetNamespace())()
}
