#!/usr/bin/env python

import json
import logging
import pycurl
import random
import sys
import time

import os

# ---------------------
# Set to True for verbose logging from pycurl
#
PY_CURL_VERBOSE=False

# -------------------------------------------------------
# Specify api key
# -------------------------------------------------------
apikey = None
try:
    apikey = os.environ['TSI_API_KEY']
    apihost = os.environ['TSI_API_HOST']

except KeyError:
    logging.error('Set the environment variable TSI_API_KEY with your TrueSight Intelligence ' +
                  'API key before running this script')
    sys.exit(1)

# -------------------------------------------------------
# Set up headers
# -------------------------------------------------------

headers = ['Expect:', 'Content-Type: application/json', 'X-API-KEY: ' + apikey]

# -------------------------------------------------
#  Generate fake numbers here.  Replace random
#  numbers with real data collection.
# -------------------------------------------------
timestamp = time.mktime(time.localtime())

browse_time = random.randrange(1, 60, 1)
bid_time = random.randrange(1, 60, 1)

browse_count = random.randrange(25, 50, 2)
bid_count = random.randrange(25, 50, 2)

# --------------------------------------------------
#  Create data structure for metrics posting
# --------------------------------------------------
myMetrics = [
    {
        "entity_type_id": "TRANSACTION",
        "entity_id": "oa-appserver-1.browse_catalog",
        "time_series": [
            {
                "metric_id": "number_of_requests",
                "values": [
                    {"v": browse_count, "t": timestamp}
                ]
            },
            {
                "metric_id": "request_response_time",
                "values": [
                    {"v": browse_time, "t": timestamp}
                ]
            }
        ]
    },
    {
        "entity_type_id": "TRANSACTION",
        "entity_id": "oa-appserver-1.bid_tx",
        "time_series": [
            {
                "metric_id": "number_of_requests",
                "values": [
                    {"v": bid_count, "t": timestamp}
                ]
            },
            {
                "metric_id": "request_response_time",
                "values": [
                    {"v": bid_time, "t": timestamp}
                ]
            }
        ]
    }
]

# -------------------------------------------------------
# Specify the uri
# -------------------------------------------------------

url = "https://{0}/api/v1/metrics?async=false".format(apihost)

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(c.VERBOSE, PY_CURL_VERBOSE)
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
data = json.dumps(myMetrics)
logging.info("data = %s" % data)
c.setopt(pycurl.POSTFIELDS, data)
c.setopt(c.SSL_VERIFYPEER, 0)
# c.setopt(pycurl.SSL_VERIFYPEER, 0)
# c.setopt(pycurl.SSL_VERIFYHOST, 0)
c.perform()
print("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

# -------------------------------------------------------
# Print the result
# -------------------------------------------------------

# print(response.status_coder)
# printr(response.textr)


logging.info("exiting....")
