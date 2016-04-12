Lab 1 - TrueSight Pulse Meters and Plugins
==========================================


## Prerequisites

- Make sure you have access to a pulse account in AMA(acronym meaning??)
- Your virtual machine has been downloaded and started. See [Virtual Machine](virtual_machine.md)
which provides the instructions for configuring and starting your virtual machine.

### Log into the Virtual Machine

1. Change directory to where you extracted the zip or cloned the repository using git.
2. Run the following command to log into the virtual machine:
```
$ vagrant ssh
```
3. After logging in you should see the following prompt:
```
$
```

## Installing the TrueSight Pulse Meter

1. Open a Web Browser
1. Log into your Pulse Account
2. Navigate to Settings => Installation
3. Copy the shell script
4. Run the shell script using `sudo`

```
$ curl -fsS -d '{"token":"<api token>"}' -H 'Content-Type: application/json' https://meter.truesight-staging.bmc.com/setup_meter > setup_meter.sh && chmod +x setup_meter.sh && ./setup_meter.sh
```
5. Once the script completes the meter will be installed. C
6. Update the `meter.conf` with the `application_id`
7. Verify data is showing in TrueSight Pulse Web Interface

## Installing the HTTP Check Plugin


## Installing the CPU Core Plugin