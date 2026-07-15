#!/usr/bin/env bash
#
# Mirrors ${SOURCE_IMAGE}:${TAG} to ${DEST_IMAGE}:${TAG} using crane. Destination
# tags are treated as immutable: if the tag already exists it is left untouched,
# so a rebuilt source image never overwrites a tag that was already published.
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

# Tags are immutable at the destination: once a tag exists we never overwrite it,
# even if the source has since been rebuilt under a new digest.
if dst_digest="$(crane digest "${dst}" 2>/dev/null)"; then
  echo "Destination ${dst} already exists -> ${dst_digest}"
  if [ "${src_digest}" = "${dst_digest}" ]; then
    echo "Destination already holds this image, nothing to do."
    echo "- \`${dst}\` already mirrored @ \`${dst_digest}\`" >> "${GITHUB_STEP_SUMMARY}"
  else
    echo "::warning::Tag ${dst} already exists with a different digest (${dst_digest}); tags are immutable, refusing to overwrite (source is ${src_digest})."
    echo "- ⚠️ \`${dst}\` already exists @ \`${dst_digest}\`; not overwritten (source @ \`${src_digest}\`)" >> "${GITHUB_STEP_SUMMARY}"
  fi
  exit 0
fi

echo "Copying ${src} -> ${dst}"
crane copy "${src}" "${dst}"

echo "- Mirrored \`${src}\` -> \`${dst}\` @ \`${src_digest}\`" >> "${GITHUB_STEP_SUMMARY}"
