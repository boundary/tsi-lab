#!/bin/bash
#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

curl -i "https://$TSP_API_HOST/v1/events" \
-X POST \
-u "$TSP_EMAIL:$TSP_API_TOKEN" \
-H "Content-Type: application/json" \
-d '{
      "title": "test event",
      "fingerprintFields": ["@title", "@message"],
      "message": "Hello World!",
      "status": "OPEN",
      "source": {"ref": "myhost", "type": "host"}
    }'
