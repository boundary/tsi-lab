#!/usr/bin/env bash
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

curl https://$TSP_API_HOST/v1/metrics \
  -X POST                             \
  -u "$TSP_EMAIL:$TSP_API_TOKEN"      \
  -H "Content-Type: application/json" \
  -d '{
         "name": "MY_COOL_METRIC",
	 "description": "A cool metric I created",
         "displayName": "My cool metric",
         "displayNameShort": "cool metric",
         "unit": "number",
         "defaultAggregate": "avg",
         "defaultResolutionMS": 1000,
         "type": "DEVICE"
      }'
