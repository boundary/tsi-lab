#!/bin/bash
set -x

# Source our environment variables that contain
# our: user, password, endpoint
if [ -r $HOME/.tsp ]
then
  source $HOME/.tsp
fi

curl -i -X POST -u "$TSP_EMAIL:$TSP_API_TOKEN" -H "Content-Type: application/json" -d '{"title": "test event", "fingerprintFields": ["@title", "@message"], "status": "OPEN", "source": {"ref": "myhost", "type": "host"}}' "https://$TSP_API_HOST/v1/events"
