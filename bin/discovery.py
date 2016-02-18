#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
#  Create an application called "Online Auction" with id "online_auc" 
#  
#  Create a device to represent the app server called "OA-AppServer-1" with id "oa-appserver-1" 
#
#  Create a type of entity to represent transactions on an app server called "Transaction" with
#  type id of "TRANSACTION" with two metrics "request_response_time" and "number_of_requests"
#
#  Create two transactions to represent activity on the appserver
#  "Bid Transaction" with id oa-appserver-1.bid-tx
#  "Browse Catalog" with id oa-appserver-1.browse_catalog
#
#  Make the metrcs number_of_requests and request_response time KPI's for the application.
# ---------------------------------------------------------------------------------------------

import json
import sys

import logging
import pycurl

import os

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

# ---------------------------------------------------------------------------------------------
#  Create the application
# ---------------------------------------------------------------------------------------------

newEntity = {
    "entity_type_id": "APPLICATION",
    "name": "Online Auction",
    "tags": [
        "app_id:online_auc"
    ],
    "cfg_attr_values": {},
    "entity_id": "online_auc",
    "source_id": "sample",
    "cfg_attr_values":
        {
            "kpis": [
                {"entity_type_id": "TRANSACTION",
                 "entity_type_name": "Transaction",
                 "entity_id": "oa-appserver-1.bid_tx",
                 "title": "Number of Requests",
                 "application_id": "online_auc",
                 "application_name": "Online Auction",
                 "metric_name": "Number of Requests",
                 "metric_uom": "#",
                 "metric_id": "number_of_requests"},
                {"entity_type_id": "TRANSACTION",
                 "entity_type_name": "Transaction",
                 "entity_id": "oa-appserver-1.bid_tx",
                 "title": "Request Response Time",
                 "application_id": "online_auc",
                 "application_name": "Online Auction",
                 "metric_name": "Request Response Time",
                 "metric_uom": "Seconds",
                 "metric_id": "request_response_time"}
            ]
        }
}

# -------------------------------------------------------
# Specify the uri
# -------------------------------------------------------

url = "https://{0}/api/v1/entities".format(apihost)

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
data = json.dumps(newEntity)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
print("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

# -------------------------------------------------------
#  Create a device
# -------------------------------------------------------

newEntity = {
    "entity_type_id": "DEVICE",
    "name": "OA-AppServer-1",
    "tags": [
        "app_id:online_auc"
    ],
    "cfg_attr_values": {},
    "entity_id": "oa-appserver-1",
    "source_id": "sample",
}

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
data = json.dumps(newEntity)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
print ("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

# -------------------------------------------------------
#  Create a monitored instance
# -------------------------------------------------------

newEntity = {
    "entity_type_id": "TRANSACTION",
    "name": "Bid Transaction",
    "tags": [
        "app_id:online_auc"
    ],
    "cfg_attr_values": {},
    "entity_id": "oa-appserver-1.bid_tx",
    "source_id": "sample",
    "parent_entity_type_id": "DEVICE",
    "parent_entity_id": "oa-appserver-1"
}

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
data = json.dumps(newEntity)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
print("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

# -------------------------------------------------------
#  Create a monitored instance
# -------------------------------------------------------

newEntity = {
    "entity_type_id": "TRANSACTION",
    "name": "Browse Catalog",
    "tags": [
        "app_id:online_auc"
    ],
    "cfg_attr_values": {},
    "entity_id": "oa-appserver-1.browse_catalog",
    "source_id": "sample",
    "parent_entity_type_id": "DEVICE",
    "parent_entity_id": "oa-appserver-1"
}

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
data = json.dumps(newEntity)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
print("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

# -------------------------------------------------------
# Create app level metrics
# -------------------------------------------------------

myMetaData = {
    "id": "TRANSACTION",
    "name": "Transaction",
    "metrics": [
        {
            "id": "number_of_requests",
            "name": "Number of Requests",
            "data_type": "number",
            "uom": "#",
            "kpi": "True",
            "key": "True",
        },
        {
            "id": "request_response_time",
            "name": "Request Response Time",
            "data_type": "number",
            "uom": "Seconds",
            "kpi": "True",
            "key": "False"
        }
    ]
}

url = "https://truesight.bmc.com/api/v1/meta"

# -------------------------------------------------------
# Issue the request
# -------------------------------------------------------

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, headers)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.SSLVERSION, pycurl.SSLVERSION_TLSv1)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
data = json.dumps(myMetaData)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
print("status code:=" + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()
