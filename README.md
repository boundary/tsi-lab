# TrueSight Intelligence Lab Environment

Vagrant lab environment for learning about TrueSight Pulse Intelligence.

Includes:
- Virtual machine environment that includes prerequisite tools for running labs
- Demonstration scripts for running labs

## Virtual Machine

The virtual machine environment is configured using vagrant.

### Prerequisites

- Vagrant 1.7.2 or later. Vagrant can be downloaded [here](https://www.vagrantup.com/downloads.html)
- VirtualBox 4.3.2.6 or later. VirtualBox can be downloaded [here](https://www.virtualbox.org/wiki/Downloads)
- Git 2.2 or later. If downloading the distribution via git. Git can be downloaded [here](http://git-scm.com/download)

### Downloading the Contents

Either clone (using git) or download the git repository [https://github.bmc.com/dgwartne/tsi-lab](https://github.bmc.com/dgwartne/tsi-lab)

#### Cloning

```
$ git clone https://github.bmc.com/dgwartne/tsi-lab
```

### Starting the Virtual Machine

With the TrueSight Intelligence api key perform issue the following command via Unix/Linux shell, or Windows command prompt:

```
$ TSP_API_KEY=<api key> vagrant up
```

### Stopping a Virtual Machine

```
$ vagrant halt
```

### Destroying a Virtual Machine

```
$ vagrant destroy
```

### Logging into the Virtual Machine



## Scripts

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


