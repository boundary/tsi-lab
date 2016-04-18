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
import pyowm
import os
import sys
import time
from tspapi import API
from tspapi import Measurement
from common import Common


class Weather(Common):
    """
    """

    def __init__(self, interval=10, cities=None):
        """
        Construct a Twitter instance

        :param interval: How often to collect stock price and volume
        :param words: Words to look for
        :return:
        """
        super(Weather, self).__init__()
        self.usage_args = 'city [city [city]...'
        self.interval = interval
        self.cities = cities
        api_key = os.environ['OWM_API_KEY']
        self.owm = pyowm.OWM(api_key)


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
            for city in self.cities:
                observation = self.owm.weather_at_place(city)
                weather = observation.get_weather()
                measurements = []
                temperature = float(weather.get_temperature('fahrenheit')['temp'])
                source = city.replace(',','_').replace(' ','_')
                properties = {"app_id": "LittleDog"}
                print('city: {0}, temperature: {1}'.format(city.replace(',','_').replace(' ','_'), temperature))
                measurements.append(Measurement(
                        metric='TEMPERATURE',
                        value=temperature,
                        source=source,
                        properties=properties))
                self.send_measurements(measurements)
            time.sleep(self.interval)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        first = True
        cities = []
        for arg in sys.argv:
            # Skip the first arguments which is the program name
            if first:
                first = False
                continue
            cities.append(arg)
        weather = Weather(interval=10, cities=cities)
        weather.run()
    else:
        Common.usage("city [[city][city]...]")
