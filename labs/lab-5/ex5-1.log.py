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
from log_utils import follow

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
