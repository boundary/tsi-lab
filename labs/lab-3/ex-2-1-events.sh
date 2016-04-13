#!/bin/bash

curl -i -X POST -u "$TSP_EMAIL:$TSP_API_TOKEN" -H "Content-Type: application/json" -d '{"title": "test event", "fingerprintFields": ["@title", "@message"], "status": "OPEN", "source": {"ref": "myhost", "type": "host"}}' "https://$TSP_API_HOST/v1/events"

curl -i "https://$TSP_API_HOST/v1/events" \
-X POST \
-u "$TSP_EMAIL:$TSP_API_TOKEN" \
-H "Content-Type: application/json" \
-d '{
      "title": "test event",
      "fingerprintFields": ["@title", "@message"],
      "status": "OPEN",
      "source": {"ref": "myhost", "type": "host"}
    }'
