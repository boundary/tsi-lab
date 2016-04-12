Lab 1 - Pulse data ingestion with Meters and Plugins
====================================================


## Prerequisites

- Make sure you have access to a pulse account in AMA(acronym meaning??)

### Starting the Virtual Machine

With the TrueSight Pulse api key perform issue the following command via Unix/Linux shell, or Windows command prompt:

```
$ TSP_API_TOKEN="<api token>" vagrant up
```

## Installing the TrueSight Pulse Meter

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