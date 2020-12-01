// +build k8srequired

package basic

import (
	"context"
	"testing"
	"time"

	"github.com/giantswarm/backoff"
	"github.com/giantswarm/microerror"
	apierrors "k8s.io/apimachinery/pkg/api/errors"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// TestNginx ensures that deployed nginx-ingress-controller is ready
func TestNginx(t *testing.T) {
	ctx := context.Background()
	var err error

	// Check nginx-ingress-controller deployment is ready.
	err = checkDeploymentReady(ctx)
	if err != nil {
		t.Fatalf("could not get deployment: %v", err)
	}
}

func checkDeploymentReady(ctx context.Context) error {
	var err error

	l.LogCtx(ctx, "level", "debug", "message", "waiting for deployment ready")

	o := func() error {
		deploy, err := appTest.K8sClient().AppsV1().Deployments(metav1.NamespaceSystem).Get(ctx, appName, metav1.GetOptions{})
		if apierrors.IsNotFound(err) {
			return microerror.Maskf(executionFailedError, "deployment %#q in %#q not found", appName, metav1.NamespaceSystem)
		} else if err != nil {
			return microerror.Mask(err)
		}

		if deploy.Status.ReadyReplicas != *deploy.Spec.Replicas {
			return microerror.Maskf(executionFailedError, "deployment %#q want %d replicas %d ready", appName, *deploy.Spec.Replicas, deploy.Status.ReadyReplicas)
		}

		return nil
	}
	b := backoff.NewConstant(2*time.Minute, 5*time.Second)
	n := backoff.NewNotifier(l, ctx)

	err = backoff.RetryNotify(o, b, n)
	if err != nil {
		return microerror.Mask(err)
	}

	l.LogCtx(ctx, "level", "debug", "message", "deployment is ready")

	return nil
}
