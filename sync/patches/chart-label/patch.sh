#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
cd "${repo_dir}"

# The upstream helm.sh/chart helper cuts "<name>-<version>" at 63 characters and trims one "-". A long
# chart version (branch builds, OCI "<tag>+<digest>") can leave the cut ending in ".", "_" or "--.",
# which is not a valid label value. Trim the whole run of "-", "." and "_".
set -x
perl -i -pe 'if (/\.Chart\.Version/ && /trunc 63/ && !/trimAll/) { s/trunc 63((?:\s*\|\s*trimSuffix\s+"[-._]")*)/trunc 63 | trimAll "-._"/ }' "helm/ingress-nginx/templates/_helpers.tpl"
{ set +x; } 2>/dev/null
