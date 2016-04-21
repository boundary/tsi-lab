#!/bin/bash
# Copyright 2014-2016 Boundary, Inc.
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

if [ -z "$TSP_EMAIL" -o -z "$TSP_API_TOKEN" -o -z "$TSP_API_HOST" ]
then
    if [ -z "$TSP_EMAIL" ]
    then
        echo 'Environment variable $TSP_EMAIL not set'
    fi

    if [ -z "$TSP_API_TOKEN" ]
    then
        echo 'Environment variable $TSP_API_TOKEN not set'
    fi

    if [ -z "$TSP_API_HOME" ]
    then
        echo 'Environment variable $TSP_API_HOME not set'
    fi
    exit 1
fi

