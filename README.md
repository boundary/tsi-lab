# TrueSight Intelligence Demo Data Tools

Location to store tools for demo data for TrueSight Intelligence.

## Contents

- discovery.py - Configures required entities
- monitor.py - Sends simulate measurement data
- env.sh - Template environment variable script


## discovery.py

1. Create an application called "Online Auction" with id "online_auc"

2. Create a device to represent the app server called "OA-AppServer-1" with id "oa-appserver-1"

3. Create a type of entity to represent transactions on an app server called "Transaction" with
type id of "TRANSACTION" with two metrics "request_response_time" and "number_of_requests"

4. Create two transactions to represent activity on the appserver:
-  "Bid Transaction" with id oa-appserver-1.bid-tx
-  "Browse Catalog" with id oa-appserver-1.browse_catalog

5. Make the metrics number_of_requests and request_response time KPI's for the application.

## monitor.py

Sends measurements to your TrueSight Intelligence instance.


## env.sh

Template script for configuring your TrueSight Intelligence API key replace your key in script:

````
export TSI_API_KEY=<put key here>
````

