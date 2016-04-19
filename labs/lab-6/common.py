#!/usr/bin/env python
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
import time
import sys
import os
from tspapi import API


class Common(object):
    def __init__(self, ):
        self.api = API()
        self.usage_args = ""
        # Set our application id from the environment variable
        self.app_id = os.environ['TSI_APP_ID']

    @staticmethod
    def usage(args):
        sys.stderr.write("usage: {0} {1}\n".format(os.path.basename(sys.argv[0]), args))

    def send_measurements(self, measurements):
        """
        Sends measurements using the Measurement API

        :param measurements:
        :return: None
        """
        self.api.measurement_create_batch(measurements)

    def run(self):
        """
        Main loop
        """
        while True:
            print("Doing absolutely nothing")
            time.sleep(self.interval)
