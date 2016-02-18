#!/bin/bash

API_URL="https://$TSI_API_HOST/api/v1/meta"

curl -1 -s -X GET -H "X-API-KEY: $TSI_API_KEY" "$API_URL" | jq .
