#!/bin/bash -l
# exit on any error
set -e

PROJECT="${INPUT_PROJECT}"
ENVIRONMENT="${INPUT_ENVIRONMENT}"
IMAGE_VERSION="${INPUT_IMAGE_VERSION}"
GITHUB_USERNAME="${GITHUB_ACTOR}"
TOKEN="${INPUT_TOKEN}"
URL="${INPUT_URL}"

prepare_payload() {
  cat <<EOF
{
    "environment_type": "${ENVIRONMENT}",
    "project_name": "${PROJECT}",
    "image_version": "${IMAGE_VERSION}",
    "github_username": "${GITHUB_USERNAME}"
}
EOF
}

response=$(curl -D headers.txt -X POST -H "Content-Type:application/json" -H "X-Api-Token:${TOKEN}" -d "$(prepare_payload)" "${URL}")

printf "HEADERS\n%s" "$(cat headers.txt)"

echo "${response}"

grep " 201" headers.txt || exit 1
