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
import os
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

def parse_apache_line(parser, line):
    """
    Uses the apachelog package to parse a line
    of a Apache HTTP server log.
    :param parser:
    :param line:
    :return:
    """
    s = None
    try:
        s = parser.parse(line)
    except apachelog.ApacheLogParserError:
        sys.stderr.write("Unable to parse %s" % line)
    return s


class LogfileParser(object):
    def __init__(self, path=None):
        """
        Constructs a Logfile parser instance given a path to a log file
        :param path:
        :return: None
        """
        # Opened handle to our log file
        self.log_file = open(path, "r")

        # Contains the text from each line append to the file
        self.line = None

    def monitor_file(self):
        """
        Monitors a file for lines append to it then calls
        a method to process the line
        :return: None
        """
        lines = monitor_file(self.log_file)
        for line in lines:
            self.line = line.strip()
            self.parse_line()

    def parse_line(self):
        """
        Default callback for processing a line which prints
        the line to standard out.
        :return: None
        """
        print(self.line)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        parser = LogfileParser()
        parser.monitor_file()
    else:
        sys.stderr.write("usage: {0} <path>".format(os.path.baseline(sys.argv[0])))
