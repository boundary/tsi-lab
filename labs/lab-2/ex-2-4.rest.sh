#!/bin/bash

curl -X POST -s "https://httpbin.org/post" \
-H "Content-Type: application/json" \
-d '{"foo": "bar", "red": true, "curly": 101}'
