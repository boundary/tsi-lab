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
import tweepy
import os
import sys
import time
from tspapi import API
from tspapi import Measurement


class Twitter(object):
    """
    """

    def __init__(self, interval=10, words=None):
        """
        Construct a Twitter instance

        :param interval: How often to collect stock price and volume
        :param words: Words to look for
        :return:
        """
        self.interval = interval
        self.words = tickers
        self.api = API()

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
            # Loop over the tickers and lookup the stock price and volume
            for word in self.words:
		print("To Be Completed")
            time.sleep(self.interval)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        first = True
        words = []
        for arg in sys.argv:
            # Skip the first arguments which is the program name
            if first:
                first = False
                continue
            tickers.append(arg)

        twitter = Twitter(interval=10, tickers=tickers)
        twitter.run()
    else:
        sys.stderr.write("usage: {0} word [word [word]...]\n".format(os.path.basename(sys.argv[0])))
