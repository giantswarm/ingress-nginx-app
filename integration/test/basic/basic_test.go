// +build k8srequired

package basic

import (
	"context"
	"testing"
)

func TestHelm(t *testing.T) {
	err := ba.Test(context.Background())
	if err != nil {
		t.Fatalf("%#v", err)
	}
}
