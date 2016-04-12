Reference
=========

- discovery.py - Configures required entities
- monitor.py - Sends simulate measurement data
- env.sh - Template environment variable script


### discovery.py

1. Create an application called "Online Auction" with id _online\_auc_

2. Create a device to represent the app server called _OA-AppServer-1_ with id _oa-appserver-1_

3. Create a type of entity to represent transactions on an app server called _Transaction_ with
type id of _TRANSACTION_ with two metrics _request\_response\_time_ and _number\_of\_requests_

4. Create two transactions to represent activity on the appserver:
   -  _Bid Transaction_ with id _oa-appserver-1.bid-tx_
   -  _Browse Catalog_ with id _oa-appserver-1.browse\_catalog_

5. Make the metrics _number\_of\_requests_ and _request\_response_ time KPI's for the application.

## monitor.py

Script that generates fake number of requests and request response time

## Configuration

### Environment variables

`TSP_API_KEY` - Contains the TrueSight Pulse API Token

## Reference

### `/etc/cron.d/monitor`

Calls the `monitor.py` script every minute.


