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
import os
import sys
import time


def follow(f):
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


if __name__ == '__main__':
    # We are expecting two arguments
    #  The first is the name of the script
    #  The second is a path to a log file
    if len(sys.argv) == 2:
        # Open our file for reading
        log_file = open(sys.argv[1], "r")
        # Create our iterable function
        log_lines = follow(log_file)
        # Process the lines as they are appended
        for line in log_lines:
            # Strip out the new line an print the line
            print("{0}".format(line.strip()))
    else:
        # Incorrect number of arguments
        # Output usage to standard out
        sys.stderr.write("usage: {0} <path>\n".format(os.path.basename(sys.argv[0])))
