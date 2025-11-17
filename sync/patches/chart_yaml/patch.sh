#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir

cd "${repo_dir}"

set -x
APP_VERSION=$(yq '.appVersion' vendor/ingress-nginx/Chart.yaml)

export APP_VERSION
yq -i e '.appVersion |= env(APP_VERSION)' helm/ingress-nginx/Chart.yaml

{ set +x; } 2>/dev/null
