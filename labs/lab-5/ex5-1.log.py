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
import sys

# %b - Size
# %h - Remote IP or Host
# %l - Remote Log Name
# %r - Request
# %>s - HTTP Status Code
# %t - eventTime
# %u - Remote User
# %{Referer}i - Referer
# %{User-agent}i - UserAgent

log_format = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}\i"'
p = apachelog.parser(log_format)

for line in open('/var/log/httpd/access_log'):
    try:
        s = p.parse(line)
        print("host: {0}, time: {1}, request: {2}, status: {3}, size: {4}, referer: {5}, agent: {6}".format(
                s['%h'], s['%t'], s['%r'], s['%>s'], s['%b'], s['%{Referer}i'], s['%{User-Agent}\\i"']))
    except apachelog.ApacheLogParserError:
        sys.stderr.write("Unable to parse %s" % line)
