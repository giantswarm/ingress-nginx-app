package basic

import (
	"fmt"
	"io"
	"net/http"
	"testing"
	"time"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"github.com/giantswarm/apptest-framework/pkg/config"
	"github.com/giantswarm/apptest-framework/pkg/state"
	"github.com/giantswarm/apptest-framework/pkg/suite"

	"github.com/giantswarm/clustertest/pkg/logger"
	"github.com/giantswarm/clustertest/pkg/wait"
)

const (
	isUpgrade = false
)

func TestBasic(t *testing.T) {
	const (
		appReadyTimeout  = 10 * time.Minute
		appReadyInterval = 5 * time.Second
	)
	suite.New(config.MustLoad("../../config.yaml")).
		WithInstallNamespace("kube-system").
		WithIsUpgrade(isUpgrade).
		WithValuesFile("./values.yaml").
		AfterClusterReady(func() {
			It("should have cert-manager and external-dns deployed", func() {
				org := state.GetCluster().Organization

				// Ingress-Nginx depends on external-dns for DNS resolution and cert-manager for certificates.
				Eventually(wait.IsAppDeployed(state.GetContext(), state.GetFramework().MC(), fmt.Sprintf("%s-cert-manager", state.GetCluster().Name), org.GetNamespace())).
					WithTimeout(appReadyTimeout).
					WithPolling(appReadyInterval).
					Should(BeTrue())

				Eventually(wait.IsAppDeployed(state.GetContext(), state.GetFramework().MC(), fmt.Sprintf("%s-external-dns", state.GetCluster().Name), org.GetNamespace())).
					WithTimeout(appReadyTimeout).
					WithPolling(appReadyInterval).
					Should(BeTrue())

				// Should we check if ingress.<baseDomain> exists?
			})
		}).
		BeforeUpgrade(func() {
			// E.g. ensure that the initial install has completed and has settled before upgrading
		}).
		Tests(func() {
			var (
				helloWorldIngressHost string
				helloWorldIngressUrl  string
			)
			BeforeEach(func() {
				helloWorldIngressHost = fmt.Sprintf("hello-world.%s", getWorkloadClusterBaseDomain())
				helloWorldIngressUrl = fmt.Sprintf("https://%s", helloWorldIngressHost)
				// org := state.GetCluster().Organization
			})

			It("should serve traffic from hello-wolrd", func() {
				// STEP
				By("creating the hello-world app CR")

				helloWorldApp, err := newHelloWorldApp(helloWorldIngressHost)
				Expect(err).To(BeNil())
				Eventually(func() (bool, error) {
					// The `ingress-nginx` app has an admission webhooks for `Ingress` resources. While the controller
					// is starting, the webhooks are not available, causing any Ingress operation to fail.
					// The `hello-world-app` fails to install during this time because it creates an Ingress resource.
					// We must wait until the deployment succeeds.

					return patchAndWait(helloWorldApp)
				}).
					WithTimeout(6 * time.Minute).
					WithPolling(5 * time.Second).
					Should(BeTrue())

				// STEP
				By("adding a LB to the ingress CR")

				Eventually(func() (bool, error) {
					return ingressHasLB("default", "hello-world")
				}).
					WithTimeout(6 * time.Minute).
					WithPolling(5 * time.Second).
					Should(BeTrue())

				// STEP
				By("serving responses from the backend")

				httpClient := newHttpClientWithProxy()
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

				// STEP
				By("uninstalling the hello-world app")

				err = state.GetFramework().MC().DeleteApp(state.GetContext(), *helloWorldApp)
				Expect(err).ShouldNot(HaveOccurred())
			})
		}).
		Run(t, "Basic Test")
}
