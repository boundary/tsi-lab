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
import logging
import json
from tspapi import API
from tspapi import Measurement
from common import Common


class Tweet(object):

    def __init__(self):
        self.created_at = None
        self.id = None
        self.text = None
        self.source = None

    def from_json(self, tweet):
        logging.info('from_json')
        if 'created_at' in tweet:
            self.created_at = tweet['created_at']

        if 'id' in tweet:
            self.id = tweet['id']

        if 'text' in tweet:
            self.text = unicode(tweet['text'])

        if 'source' in tweet:
            self.source = tweet['source']

    def __unicode__(self):
        return "created_at: {0}, id: {1}, text: {2}, source: {3}".format(self.created_at,
                                                                         self.id,
                                                                         self.text,
                                                                         self.source)

    def __str__(self):
        u = ''
        try:
            u = unicode(self).encode('utf-8')
        except UnicodeEncodeError as e:
            logging.error("UNICODE: {0}".format(e))
        return u


class Twitter(tweepy.StreamListener, Common):
    """
    """

    def __init__(self, words=None):
        """
        Construct a Twitter instance

        :param words: Words to look for in the Twitter stream
        :return:
        """
        super(Twitter, self).__init__()
        self.words = words
        self.api = API()

    def on_data(self, data):
        try:
            tweet = Tweet()
            tweet.from_json(json.loads(data.encode('utf-8')))
            logging.info(tweet.id)
            logging.info(tweet.text)
            logging.info(tweet.source)
        except UnicodeEncodeError as e:
            logging.error(e)

    def on_error(self, status_code):
        logging.error("status_code: {0}".format(status_code))
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def send_measurements(self, measurements):
        """
        Sends measurements using the Measurement API

        :param measurements:
        :return: None
        """
        self.api.measurement_create_batch(measurements)

    def run(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Start")

        logging.info("get keys")
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        access_token = os.environ['ACCESS_TOKEN']
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

        logging.info("set auth")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        logging.info("stream")
        stream = tweepy.Stream(auth=auth, listener=Twitter())
        stream.filter(track=self.words)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        first = True
        words = []
        for arg in sys.argv:
            # Skip the first arguments which is the program name
            if first:
                first = False
                continue
            words.append(arg)

        twitter = Twitter(words=words)
        twitter.run()
    else:
        Common.usage('word [word [word]...]')
