package hello_world

import (
	"context"
	"fmt"
	"io"
	"net"
	"net/http"
	"net/url"
	"os"
	"testing"
	"time"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"github.com/giantswarm/apiextensions-application/api/v1alpha1"
	"github.com/giantswarm/apptest-framework/pkg/config"
	"github.com/giantswarm/apptest-framework/pkg/state"
	"github.com/giantswarm/apptest-framework/pkg/suite"
	"github.com/giantswarm/clustertest/pkg/application"
	"github.com/giantswarm/clustertest/pkg/logger"
	"github.com/giantswarm/clustertest/pkg/wait"

	networkingv1 "k8s.io/api/networking/v1"
	"k8s.io/apimachinery/pkg/types"
	ctrl "sigs.k8s.io/controller-runtime/pkg/client"
)

const (
	isUpgrade = false
)

func TestHelloWorld(t *testing.T) {

	var (
		helloWorldApp         *application.Application
		helloWorldIngressHost string
		helloWorldIngressUrl  string
	)
	const (
		appReadyTimeout  = 3 * time.Minute
		appReadyInterval = 5 * time.Second
	)
	suite.New(config.MustLoad("../../config.yaml")).
		WithInstallNamespace("kube-system").
		WithIsUpgrade(isUpgrade).
		WithValuesFile("./values.yaml").
		BeforeInstall(func() {
			// Do any pre-install checks here (ensure the cluster has needed pre-reqs)
			It("should have cert-manager and external-dns deployed", func() {
				org := state.GetCluster().Organization

				// The hello-world app ingress requires a `Certificate` and a DNS record, so we need to make sure `cert-manager` and `external-dns` are deployed.
				Eventually(wait.IsAppDeployed(state.GetContext(), state.GetFramework().MC(), fmt.Sprintf("%s-cert-manager", state.GetCluster().Name), org.GetNamespace())).
					WithTimeout(appReadyTimeout).
					WithPolling(appReadyInterval).
					Should(BeTrue())

				Eventually(wait.IsAppDeployed(state.GetContext(), state.GetFramework().MC(), fmt.Sprintf("%s-external-dns", state.GetCluster().Name), org.GetNamespace())).
					WithTimeout(appReadyTimeout).
					WithPolling(appReadyInterval).
					Should(BeTrue())
			})
		}).
		BeforeUpgrade(func() {
			// Perform any checks between installing the latest released version
			// and upgrading it to the version to test
			// E.g. ensure that the initial install has completed and has settled before upgrading
		}).
		Tests(func() {
			Context("hello world", Ordered, func() {
				It("should deploy the hello-world app", func() {
					org := state.GetCluster().Organization

					helloWorldIngressHost = fmt.Sprintf("hello-world.%s", getWorkloadClusterDnsZone())
					helloWorldIngressUrl = fmt.Sprintf("https://%s", helloWorldIngressHost)
					helloAppValues := map[string]string{"IngressUrl": helloWorldIngressHost}

					helloWorldApp = application.New(fmt.Sprintf("%s-hello-world", state.GetCluster().Name), "hello-world").
						WithCatalog("giantswarm").
						WithOrganization(*org).
						WithVersion("latest").
						WithClusterName(state.GetCluster().Name).
						WithInCluster(false).
						WithInstallNamespace("default").
						MustWithValuesFile("./test_data/helloworld_values.yaml", &application.TemplateValues{
							ClusterName:  state.GetCluster().Name,
							Organization: state.GetCluster().Organization.Name,
							ExtraValues:  helloAppValues,
						})

					err := state.GetFramework().MC().DeployApp(state.GetContext(), *helloWorldApp)
					Expect(err).To(BeNil())

					Eventually(func() (bool, error) {
						// The `ingress-nginx` app has an admission webhooks for `Ingress` resources. While the controller
						// is starting, the webhooks are not available, causing any Ingress operation to fail.
						// The `hello-world-app` fails to install during this time because it creates an Ingress resource.
						// We must wait until the deployment succeeds.

						return waitWithPatch(helloWorldApp)
					}).
						WithTimeout(6 * time.Minute).
						WithPolling(5 * time.Second).
						Should(BeTrue())
				})
				It("ingress resource has load balancer in status", func() {
					wcClient, err := state.GetFramework().WC(state.GetCluster().Name)
					Expect(err).ShouldNot(HaveOccurred())

					Eventually(func() (bool, error) {
						logger.Log("Checking if ingress has load balancer set in status")
						helloIngress := networkingv1.Ingress{}
						err := wcClient.Get(state.GetContext(), types.NamespacedName{Name: "hello-world", Namespace: "default"}, &helloIngress)
						if err != nil {
							logger.Log("Failed to get ingress: %v", err)
							return false, err
						}

						if helloIngress.Status.LoadBalancer.Ingress != nil &&
							len(helloIngress.Status.LoadBalancer.Ingress) > 0 &&
							helloIngress.Status.LoadBalancer.Ingress[0].Hostname != "" {

							logger.Log("Load balancer hostname found in ingress status: %s", helloIngress.Status.LoadBalancer.Ingress[0].Hostname)
							return true, nil
						}

						return false, nil
					}).
						WithTimeout(6 * time.Minute).
						WithPolling(5 * time.Second).
						Should(BeTrue())
				})

				It("hello world app responds successfully", func() {
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

					Eventually(func() (string, error) {
						logger.Log("Trying to get a successful response from %s", helloWorldIngressUrl)
						resp, err := httpClient.Get(helloWorldIngressUrl)
						if err != nil {
							return "", err
						}
						defer resp.Body.Close()

						if resp.StatusCode != http.StatusOK {
							logger.Log("Was expecting status code '%d' but actually got '%d'", http.StatusOK, resp.StatusCode)
							return "", err
						}

						bodyBytes, err := io.ReadAll(resp.Body)
						if err != nil {
							logger.Log("Was not expecting the response body to be empty")
							return "", err
						}

						return string(bodyBytes), nil
					}).
						WithTimeout(15 * time.Minute).
						WithPolling(5 * time.Second).
						Should(ContainSubstring("Hello World"))
				})

				It("uninstall apps", func() {
					err := state.GetFramework().MC().DeleteApp(state.GetContext(), *helloWorldApp)
					Expect(err).ShouldNot(HaveOccurred())
				})
			})
		}).
		Run(t, "Hello World Test")
}

func getWorkloadClusterDnsZone() string {
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
