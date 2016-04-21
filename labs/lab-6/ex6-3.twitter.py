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
from ConfigParser import SafeConfigParser


class Tweet(object):
    """
    A utility class that stores some of the selected fields of a Tweet

    The fields:

        created_at: When the tweet was published
        id: Unique id of the tweet
        text: Text of the tweet
        source: Source of the tweet

    """

    def __init__(self):
        """
        Initialize a Tweet instance
        :return: None
        """
        self.created_at = None
        self.id = None
        self.text = None
        self.source = None

    def from_json(self, tweet):
        """
        Converts the JSON Tweet document to dictionary and assign to member variables

        :param tweet: Unicode JSON document
        :return: None
        """
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
        """
        Return a Unicode string representing this Tweet

        :return: unicode
        """
        return "created_at: {0}, id: {1}, text: {2}, source: {3}".format(self.created_at,
                                                                         self.id,
                                                                         self.text,
                                                                         self.source)

    def __str__(self):
        """
        Create a string representation of the Tweet.

        :return: str
        """
        u = ''
        try:
            u = unicode(self).encode('utf-8')
        except UnicodeEncodeError as e:
            logging.error("UNICODE: {0}".format(e))
        return u


class Twitter(tweepy.StreamListener, Common):
    """
    Listener called by the Tweepy API and uses are Common class used in
    the Lab 6 exercises
    """

    def __init__(self, words=None, config_file='ex6-3.twitter.config'):
        """
        Construct a Twitter instance

        :param words: Words to look for in the Twitter stream
        :param config_file: File that contains the twitter keys
        :return: None
        """

        # Call our parent __init__() function so that they get initializes
        super(Twitter, self).__init__()

        # Array of words passed on the command line to look for in the Twitter stream
        self.words = words

        # Look for the config file in the same directory where this file is located
        self.config_file = os.path.join(os.path.dirname(__file__), config_file)

        # Variables to store the Twitter keys
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_token_secret = None

    def on_data(self, data):
        """
        This gets called whenever data is available on the Twitter stream
        :param data:
        :return:
        """
        try:
            tweet = Tweet()
            tweet.from_json(json.loads(data.encode('utf-8')))
            logging.info(tweet.id)
            logging.info(tweet.text)
            logging.info(tweet.source)
        except UnicodeEncodeError as e:
            logging.error(e)

    def on_error(self, status_code):
        """
        If any occurs than the Tweepy API calls this method on our instance
        :param status_code: HTTP status code
        :return: None
        """
        logging.error("status_code: {0}".format(status_code))
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def read_configuration(self):
        parser = SafeConfigParser()
        parser.read(self.config_file)
        print(parser.get('Twitter', 'consumer_key'))
        print(parser.get('Twitter', 'consumer_secret'))
        print(parser.get('Twitter', 'access_token'))
        print(parser.get('Twitter', 'access_secret_token'))

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
