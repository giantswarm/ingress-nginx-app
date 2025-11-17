#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly dir
cd "${dir}/.."

# Stage 1 sync - intermediate to the ./vendir folder
set -x
vendir sync
{ set +x; } 2>/dev/null

# Patches
./sync/patches/helpers/patch.sh
./sync/patches/proxy-protocol-configmap/patch.sh
./sync/patches/services/patch.sh
./sync/patches/values/patch.sh
./sync/patches/chart_yaml/patch.sh
./sync/patches/readme/patch.sh # should be always the last entry

# Store diffs
rm -f ./diffs/*
for f in $(git --no-pager diff --no-exit-code --no-color --no-index vendor/ingress-nginx helm/ingress-nginx --name-only) ; do
        [[ "$f" == "helm/ingress-nginx/Chart.yaml" ]] && continue
        [[ "$f" == "helm/ingress-nginx/README.md" ]] && continue
        [[ "$f" == "helm/ingress-nginx/values.schema.json" ]] && continue
        [[ "$f" == "helm/ingress-nginx/.kube-linter.yaml" ]] && continue

        base_file="vendor/ingress-nginx/${f#"helm/"}"
        [[ ! -e $base_file ]] && base_file="vendor/${f#"helm/"}"
        [[ ! -e $base_file ]] && base_file="/dev/null"

        set +e
        set -x
        git --no-pager diff --no-exit-code --no-color --no-index "$base_file" "${f}" \
                > "./diffs/${f//\//__}.patch" # ${f//\//__} replaces all "/" with "__"

        { set +x; } 2>/dev/null
        set -e
        ret=$?
        if [ $ret -ne 0 ] && [ $ret -ne 1 ] ; then
                exit $ret
        fi
done
