# TrueSight Intelligence Demo Data Tools

Location to store tools for demo data for TrueSight Intelligence.

## Contents

- discovery.py - Configures required entities
- monitor.py - Sends simulate measurement data
- env.sh - Template environment variable script


## discovery.py

1. Create an application called "Online Auction" with id _online\_auc_

2. Create a device to represent the app server called _OA-AppServer-1_ with id _oa-appserver-1_

3. Create a type of entity to represent transactions on an app server called _Transaction_ with
type id of _TRANSACTION_ with two metrics _request\_response\_time_ and _number\_of\_requests_

4. Create two transactions to represent activity on the appserver:
   -  _Bid Transaction_ with id _oa-appserver-1.bid-tx_
   -  _Browse Catalog_ with id _oa-appserver-1.browse\_catalog_

5. Make the metrics _number\_of\_requests_ and _request\_response_ time KPI's for the application.

## monitor.py

Sends measurements to your TrueSight Intelligence instance.

#### Running the script in cron

1. Create a soft link to the versioned directory

   ````
   $ ln -fs tsi-demo-tools-x.x.x tsi-demo-tools
   ````
2. Add the crontab entry with the following

   ````
   # Run script every minute
   */1 * * * * $HOME/tsi-demo-tools/monitor.py
   ````

## env.sh

Template script for configuring your TrueSight Intelligence API key replace your key in script:

   ````
export TSI_API_KEY=<put key here>
   ````

