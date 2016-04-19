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
import ystockquote
import os
import sys
import time
from tspapi import API
from tspapi import Measurement
from common import Common


class Ticker(Common):
    """
    Collects the current stock price and volume from ticker
    """

    def __init__(self, interval=10, tickers=None):
        """
        Construct a Ticker instance

        :param interval: How often to collect stock price and volume
        :return:
        """
        super(Ticker, self).__init__()
        self.interval = interval
        self.tickers = tickers

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
        properties = {"app_id": self.app_id}
        while True:
            # Loop over the tickers and lookup the stock price and volume
            for ticker in self.tickers:
                measurements = []
                price = ystockquote.get_price(ticker)
                volume = ystockquote.get_volume(ticker)
                timestamp = int(time.time())
                if volume == 'N/A' or price == 'N/A':
                    sys.stderr.write('Could not find ticker \"{0}\", skipping'.format(ticker))
                else:
                    print("ticker: {0}, price: {1}, volume: {2}".format(ticker, price, volume))
                    measurements.append(Measurement(metric='STOCK_PRICE',
                                                    value=price,
                                                    source=ticker,
                                                    properties=properties))
                    measurements.append(Measurement(metric='STOCK_VOLUME',
                                                    value=volume,
                                                    source=ticker,
                                                    properties=properties))
                    self.send_measurements(measurements)
            time.sleep(self.interval)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        first = True
        tickers = []
        for arg in sys.argv:
            # Skip the first arguments which is the program name
            if first:
                first = False
                continue
            tickers.append(arg)

        stocks = Ticker(interval=10, tickers=tickers)
        stocks.run()
    else:
        sys.stderr.write("usage: {0} ticker [ticker [ticker]...]\n".format(os.path.basename(sys.argv[0])))
