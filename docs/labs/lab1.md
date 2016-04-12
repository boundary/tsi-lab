Lab 1 - TrueSight Pulse Meters and Meter Plugins
================================================

## Overview

These exercises introduce you to the TrueSight Pulse Meter and Plugins with step by step instructions
on how to install the meter and two meter plugins.


## Prerequisites

- Make sure you have access to a pulse account in AMA(acronym meaning??)
- Your virtual machine has been downloaded and started. See [Virtual Machine](virtual_machine.md)
which provides the instructions for configuring and starting your virtual machine.

## Exercise 1-1 Installing a Meter

### Log into the Virtual Machine

1. Change directory to where you extracted the zip or cloned the repository using git.
2. Run the following command to log into the virtual machine:
```
$ vagrant ssh
```
After logging in you should see the following prompt:
```
Last login: Tue Apr 12 13:51:40 2016 from 10.0.2.2
[vagrant@tsi-lab-01 ~]$
```

which indicates you have a `bash` shell up and ready to receive commands.

### Installing the TrueSight Pulse Meter

1. Open a Chrome Web Browser to [https://truesight-staging.bmc.com](https://truesight-staging.bmc.com)
2. Login using your e-mail and password.
3. Click on the link [Open pulse.truesight-staging.bmc.com](https://pulse.truesight-staging.bmc.com/)
4. Navigate to _Settings_ by clicking on the third icon from bottom left of the screen
that looks like a gear.
5. Click on the _Installation_ link just below the label _Help With:_
6. Copy the shell script in the User Interface
7. Type `sudo` in your virtual machine bash shell.
8. Next paste the script contents after `sudo` in your virtual machine bash shell and
post fix with `-s`. After this step your command line will resemble the following:
```
[vagrant@tsi-lab-01 ~]$ sudo curl -fsS -d '{"token":"ab75f2fa-d391-4695-9dc7-a9469886f08c"}' \
-H 'Content-Type: application/json' \
https://meter.truesight-staging.bmc.com/setup_meter > setup_meter.sh \
&& chmod +x setup_meter.sh && ./setup_meter.sh -s
```
9. Hit return to run the command
10. A successful meter installation will end with:
```
The meter has been installed successfully!
[vagrant@tsi-lab-01 ~]$
```

### Updating the `meter.conf` with `application_id`

1. Update the meter configuration `/etc/boundary/meter.conf` with the `application_id` as shown
in this configuration snippet:
```
    "properties":{
      "application_id": "FOOBAR"
    },
```
2. Restart the meter to have the change take affect:
```
[vagrant@tsi-lab-01 ~]$ sudo service boundary-meter restart
Restarting boundary-meter (via systemctl):                 [  OK  ]
```
3. Open your Chrome Web Browser to
[https://pulse.truesight-staging.bmc.com/home](https://pulse.truesight-staging.bmc.com/home)
to verify that measurements are being sent to your TrueSight Pulse dashboards.


## Exercise 1-2 - Meter Plugins

This exercise will have you install 2 meter plugins:

- HTTP Check - Measures the response time of multiple HTTP endpoints
- CPU Core - Provides CPU Utilization per CPU core.

### Installing the HTTP Check Plugin

1. The HTTP Check Plugin can be installed by following the video
[here](https://help.truesight.bmc.com/hc/en-us/articles/202622071-Plugins-HTTP-Check-Deployment-Walkthrough)

2. After configuring the HTTP Check Plugin confirm data is being streamed by opening the _HTTP Check_
dashboard.


### Installing the CPU Core Plugin

1. The CPU Core can be installed by the following the video
[](https://help.truesight.bmc.com/hc/en-us/articles/202671691-Plugins-CPU-Core-Deployment-Walkthrough)

2. After configuring the CPU Core Plugin confirm data is being streamed by opening the _CPU Core_
dashboard.
