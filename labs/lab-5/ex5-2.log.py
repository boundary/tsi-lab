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
import time
import sys


def follow(f):
    """
    Reads a line from a file when available
    :param f: open file
    :return: a line from the file
    """
    f.seek(0, 2)
    while True:
        log_line = f.readline()
        if not log_line:
            time.sleep(0.1)
            continue
        yield log_line

if __name__ == '__main__':
    if len(sys.argv) > 1:
        log_file = open(sys.argv[1], "r")
        log_lines = follow(log_file)
        for line in log_lines:
            print("{0}".format(line.strip()))
