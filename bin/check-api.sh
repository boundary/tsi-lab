#!/bin/bash

if [ $# -ne 1 ]
then
  if [ -z "$TSI_API_TOKEN" ]
  then
    echo "usage: $(basename $0) <api key>"
  else
    API_KEY=$TSI_API_TOKEN
  fi
else
  API_KEY="$1"
fi

API_HOST=truesight.bmc.com
API_PATH=api/v1/meta
API_URL="https://$API_HOST/$API_PATH"

curl -1 -s -X GET -H "X-API-KEY: $API_KEY" "$API_URL" | jq .
