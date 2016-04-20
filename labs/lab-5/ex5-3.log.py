#!/usr/bin/env python
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
import apachelog
import os
import sys
from log_utils import LogfileParser, parse_apache_line
from tspapi import API
from tspapi import Measurement


class ApacheLogfileParser(LogfileParser):
    def __init__(self, path=None):
        super(ApacheLogfileParser, self).__init__(path)
        log_format = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}\i"'
        self.parser = apachelog.parser(log_format)
        self.api = API()

    def send_measurements(self, measurements):
        """
        Sends measurements to standard out to be read by plugin manager

        :param measurements:
        :return: None
        """
        self.api.measurement_create_batch(measurements)

    def parse_line(self):
        """
        Parse each of the lines of the Apache HTTP server access log.
        :return:
        """
        parsed = parse_apache_line(self.parser, self.line)
        measurements = []
        user_agent = parsed['%{User-Agent}\i"']
        bytes = int(parsed['%b'])
        status_code = parsed['%>s']
        properties = {"app_id", self.app_id}
        # Split the line by spaces and get the request in the first value
        request = parsed['%r'].split(' ')[0]
        print("user_agent: {0}, bytes: {1}, request: {2}, status_code: {3}".format(
                user_agent, bytes, request, status_code))

        measurements.append(Measurement(
                metric='HTTP_REQUESTS',
                value=1, source=request,
                properties=properties))
        measurements.append(Measurement(
                metric='HTTP_BYTES',
                value=bytes,
                source=user_agent,
                properties=properties))
        self.send_measurements(measurements)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        parser = ApacheLogfileParser(path=sys.argv[1])
        parser.monitor_file()
    else:
        sys.stderr.write("usage: {0} path\n".format(os.path.basename(sys.argv[0])))
