#!/usr/bin/python
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
import sys
import time


def monitor_file(f):
    """
    Reads a line from a file when available
    :param f: open file
    :return: a line from the file
    """
    # Go to the end of the file
    f.seek(0, 2)

    # Loop waiting for lines to be written
    while True:
        log_line = f.readline()
        # If there is nothing to read then wait a bit
        # and try again
        if not log_line:
            time.sleep(0.1)
            continue
        # We have a line return the line
        yield log_line


# %b - Size
# %h - Remote IP or Host
# %l - Remote Log Name
# %r - Request
# %>s - HTTP Status Code
# %t - eventTime
# %u - Remote User
# %{Referer}i - Referer
# %{User-agent}i - UserAgent

# log_format = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}\i"'
# p = apachelog.parser(log_format)


def parse_apache_line(parser, line):
    s = None
    try:
        s = parser.parse(line)
    except apachelog.ApacheLogParserError:
        sys.stderr.write("Unable to parse %s" % line)
    return s
