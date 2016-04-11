#!/bin/bash
set -x

# Source our environment variables that contain
# our: user, password, endpoint
source $HOME/.tsp

curl -X GET -u "$TSP_EMAIL:$TSP_API_TOKEN" -d '{"title": "test", "fingerprint_Fields="@title", "source": {"ref": "myhost", "type": "host}' "https://$TSP_API_HOST/v1/events"
