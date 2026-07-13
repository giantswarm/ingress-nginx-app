#!/usr/bin/env bash
#
# Mirrors ${SOURCE_IMAGE}:${TAG} to ${DEST_IMAGE}:${TAG} using crane, skipping
# the copy when the destination already holds the same digest.
#
# Expects the following environment variables and an authenticated crane
# (source and destination logins performed by the calling workflow):
#   SOURCE_IMAGE - source repository, without tag
#   DEST_IMAGE   - destination repository, without tag
#   TAG          - tag to mirror
set -euo pipefail

: "${SOURCE_IMAGE:?SOURCE_IMAGE must be set}"
: "${DEST_IMAGE:?DEST_IMAGE must be set}"
: "${TAG:?TAG must be set}"

src="${SOURCE_IMAGE}:${TAG}"
dst="${DEST_IMAGE}:${TAG}"

src_digest="$(crane digest "${src}")"
echo "Source ${src} -> ${src_digest}"

if dst_digest="$(crane digest "${dst}" 2>/dev/null)"; then
  echo "Destination ${dst} -> ${dst_digest}"
  if [ "${src_digest}" = "${dst_digest}" ]; then
    echo "Destination already up to date, nothing to do."
    echo "- \`${src}\` already mirrored to \`${dst}\` @ \`${src_digest}\`" >> "${GITHUB_STEP_SUMMARY}"
    exit 0
  fi
fi

echo "Copying ${src} -> ${dst}"
crane copy "${src}" "${dst}"

echo "- Mirrored \`${src}\` -> \`${dst}\` @ \`${src_digest}\`" >> "${GITHUB_STEP_SUMMARY}"
