#!/bin/bash

curl -X PUT -s "https://httpbin.org/put" \
-H "Content-Type: application/json" \
-d '{"foo": "bar", "red": true, "curly": 101}'
