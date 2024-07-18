#!/usr/bin/env python

import os
import sys
from urllib import parse
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

PROJECT = os.environ.get("INPUT_PROJECT")
ENVIRONMENT = os.environ.get("INPUT_ENVIRONMENT")
IMAGE_VERSION = os.environ.get("INPUT_IMAGE_VERSION")
GITHUB_USERNAME = os.environ.get("GITHUB_ACTOR")
URL = os.environ.get("INPUT_URL")


def main():
    uri = urlparse(URL)
    token = uri.username
    # remove token because it will be send in headers
    url = uri.geturl().replace(f"{token}@", "")

    payload = {
        "environment_type": ENVIRONMENT,
        "project_name": PROJECT,
        "image_version": IMAGE_VERSION,
        "github_username": GITHUB_USERNAME,
    }
    data = parse.urlencode(payload).encode()
    request = Request(url, headers={"X-Api-Key": str(token)}, data=data)
    try:
        with urlopen(request) as response:
            if response.status == 201:
                uid = response.read().decode().strip()
                deployment_url = uri.geturl().replace(uri.path, f"/deployments/{uid}")
                sys.stdout.write(
                    f"Deployment created with uid: {uid}, your can see its details in {deployment_url}\n"
                )
    except HTTPError as error:
        sys.stderr.write(f"HTTP Error: {error.reason} {error.read().decode()}")
        sys.exit(1)


if __name__ == "__main__":
    main()
