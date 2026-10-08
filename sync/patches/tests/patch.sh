#!/usr/bin/env bash
#
# Upstream ships its chart unit tests next to the chart, and vendir brings them
# in along with the templates. Two classes of expectation do not survive the
# trip, so they are rewritten here rather than edited in place -- a direct edit
# to helm/ingress-nginx/tests/ is lost on the next `vendir sync`.
#
#   1. Image references. Upstream pulls from registry.k8s.io; we mirror into
#      gsoci.azurecr.io under different repository names.
#   2. Values we default differently from upstream. `controller.autoscaling.enabled`
#      is false upstream and true here, and `controller.replicaCount` differs too,
#      so a test that says nothing about them renders a different manifest here
#      than it did upstream. Each affected suite pins the upstream value, and a
#      test that sets the key itself keeps its own value.
#
set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
tests_dir="${repo_dir}/helm/ingress-nginx/tests"
cd "${repo_dir}"
set -x

# 1. image expectations
sed -i \
  -e 's|registry\.k8s\.io/ingress-nginx/controller|gsoci.azurecr.io/giantswarm/ingress-nginx-controller|g' \
  -e 's|registry\.k8s\.io/defaultbackend-amd64|gsoci.azurecr.io/giantswarm/defaultbackend|g' \
  -e 's|registry\.k8s\.io/custom-repo/custom-image|gsoci.azurecr.io/custom-repo/custom-image|g' \
  -e 's|custom\.registry\.io/ingress-nginx/controller|custom.registry.io/giantswarm/ingress-nginx-controller|g' \
  -e 's|custom\.registry\.io/defaultbackend-amd64|custom.registry.io/giantswarm/defaultbackend|g' \
  "${tests_dir}"/controller-daemonset_test.yaml \
  "${tests_dir}"/controller-deployment_test.yaml \
  "${tests_dir}"/default-backend-deployment_test.yaml

# 2. upstream defaults, pinned per suite. `select(has(...) | not)` leaves a test
#    that sets the key itself untouched. The operator must be `|=`: with plain
#    `=`, yq evaluates the right side against the left side's context, where a
#    bare literal resolves to nothing and the key lands as null.
for f in controller-deployment_test.yaml controller-keda_test.yaml controller-poddisruptionbudget_test.yaml ; do
  yq -i '
    (.tests[] | select(has("set") | not)).set = {} |
    (.tests[].set | select(has("controller.autoscaling.enabled") | not))."controller.autoscaling.enabled" |= false
  ' "${tests_dir}/${f}"
done

yq -i '
  (.tests[].set | select(has("controller.replicaCount") | not))."controller.replicaCount" |= 1
' "${tests_dir}/controller-poddisruptionbudget_test.yaml"

{ set +x; } 2>/dev/null
