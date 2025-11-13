#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
chart_dir="${repo_dir}/helm/ingress-nginx"

cd "${repo_dir}"

set -x

# Replace blank lines with a temporary marker
sed -i '/^$/s// #BLANK_LINE#/' "${chart_dir}/values.yaml"

sed -i '0,/  minAvailable/s/^\  minAvailable: 1/\  # minAvailable: 1/' "${chart_dir}/values.yaml"
sed -i '0,/  # maxUnavailable/s/^\  # maxUnavailable: 1/\  maxUnavailable: "25%"/' "${chart_dir}/values.yaml"


yq -i '. *= load("sync/patches/values/values.yaml")' "${chart_dir}/values.yaml"

# Restore blank lines
# Keep placeholder "#BLANK_LINE#" lines as blanks, but delete other empty/whitespace-only lines:
# 1) Make placeholder lines non-empty so they survive deletion
# 2) Delete truly empty / whitespace-only lines
# 3) Remove the placeholder marker to turn those lines back into real blanks
sed -i -E '
  s/^#BLANK_LINE#$/ #BLANK_LINE#/;
  /^[[:space:]]*$/d;
  s/[[:space:]]*#BLANK_LINE#$//
' "${chart_dir}/values.yaml"

# Cosmetics
sed -i '/^[[:space:]]\{4\}## Overrides for generated resource names$/,/^[[:space:]]\{4\}# fullnameOverride:$/ s/^[[:space:]]\{4\}//' "${chart_dir}/values.yaml"

## Remove topologySpreadConstraints comment
{
  start_line="$(grep -n -m1 '^  # - labelSelector:' ${chart_dir}/values.yaml | cut -d: -f1)"
  end_line="$(awk -v s="$start_line" 'NR>s { if ($0 ~ /^[[:space:]]*$/) { print NR-1; exit } }' ${chart_dir}/values.yaml)"
  sed -i "${start_line},${end_line}d" "${chart_dir}/values.yaml"
}

{ set +x; } 2>/dev/null
