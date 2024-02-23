package basic

import (
	"testing"

	// . "github.com/onsi/ginkgo/v2"
	// . "github.com/onsi/gomega"

	"github.com/giantswarm/apptest-framework/pkg/config"
	"github.com/giantswarm/apptest-framework/pkg/suite"
)

const (
	isUpgrade = false
)

func TestBasic(t *testing.T) {
	suite.New(config.MustLoad("../../config.yaml")).
		WithInstallNamespace("kube-system").
		WithIsUpgrade(isUpgrade).
		WithValuesFile("./values.yaml").
		BeforeInstall(func() {
			// Do any pre-install checks here (ensure the cluster has needed pre-reqs)
		}).
		BeforeUpgrade(func() {
			// Perform any checks between installing the latest released version
			// and upgrading it to the version to test
			// E.g. ensure that the initial install has completed and has settled before upgrading
		}).
		Tests(func() {
			// Include calls to app tests here
		}).
		Run(t, "Basic Test")
}
