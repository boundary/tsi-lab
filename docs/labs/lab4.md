Lab 4 - Metric and Measurement APIs
===================================

## Overview

This lab will introduce you to the Metric and Measurement APIs by showing you how to
extracting example business data from a MySQL database and sending the business data
to TrueSight Intelligence.

### Metrics versus Measurements

_Metrics_ and _Measurements_ are often used interchangeable by in the context of the TrueSight Intelligence APIs
we need to make a distinction as follows:

- *Metrics* are the *definition* of what the time series represents
- *Measurements* are the *actual* time series values that are collected

#### Metric

A metric definitions consists of the following:

- Name
- Display Name
- Display Name Short
- Description
- Default Aggregate
- Default Resolution
- Type
- Units

##### Name

This is the primary key and is used to uniquely identify each metric in an account. The name is all
uppercase with addition of underscores(`_`) and periods('.'). Some of the built-in metrics include:
CPU, Network In, or Data Disk Out.

##### Display Name

Label to identify the metric in the user interface or other place where user readable text is needed.

##### Display Name Short

Same use as _Display Name_ but in those cases where shortened text is required (limit to 20 characters).

##### Description

Provides textual information or other information relevant in describing the metric.

##### Default Aggregate

When graphing the metric that makes the most sense, which is one of:

- Average
- Minimum
- Maximum
- Sum

##### Type

TrueSight Intelligence entity type

##### Unit

This field consists of an enumerated type the describes the unit of meaurement of the metric. The types
consist of the following;

- ByteCount
- Duration
- Number
- Percent

_NOTE_: _Duration_ is milliseconds and is not current configurable. Percent is given in decimal form, for
example %63.2 would be given as 0.632.

#### Measurements

Are the time series data collected for a particular _metric_ which are made of the following:

- Metric
- Value
- Source
- Timestamp

##### Metric

Refers to the specific _Metric_ of the Measurement

##### Value

Value of the metric at the given timestamp. If the Metric unit is _percent_ then this is value in its
decimal equivalent.

##### Source

Most often the system hostname but it is used to indicate the specific instance of the thing being measured. For
example if were measuring individual utilization for CPU cores the source would refer to the specific core.

##### Timestamp

When the measurement occurred in [UNIX epoch time](https://en.wikipedia.org/wiki/Unix_time) which is either
in seconds or milliseconds.

##### Properties

In addition to the previously discussed Measurement fields, there are optional fields for further
classification of a measurement.

The _Application Id_ is used to organize data in TrueSight Intelligence.

**To Be Discussed**

## Metric and Measurement APIs

Online documentation of the Metric and Measurement APIs is located
[here](https://documentation.truesight.bmc.com/overview)

### Metric API

This section goes into the nuts and bolts of defining metrics several ways
using the Metric API.


#### Creating a Metric definition with `curl`

Metric definitions can be created with the _curl_ as shown here.

```
curl https://$TSP_API_HOST/v1/metrics \
  -X POST                             \
  -u "$TSP_EMAIL:$TSP_API_TOKEN"      \
  -H "Content-Type: application/json" \
  -d '{
         "name": "MY_COOL_METRIC",
         "description": "A cool metric I created",
         "displayName": "My cool metric",
         "displayNameShort": "cool metric",
         "unit": "number",
         "defaultAggregate": "avg",
         "defaultResolutionMS": 1000,
         "type": "DEVICE"
      }'
```

#### Creating a Metric definition with `metric-create`

The command line version of metric create can be used to create a metric definition running the following:

```
$ metric-create -n CLI_METRIC -d "CLI metric"  -s "CLI metric" -g avg -u number -y DEVICE
```

which results in the following output:

```
{
  "result": {
    "name": "CLI_METRIC",
    "displayName": "CLI metric",
    "displayNameShort": "CLI metric",
    "unit": "number",
    "defaultAggregate": "AVG",
    "type": "DEVICE",
    "id": 1444
  }
}
```

_NOTE_: metric-create as are all of the CLIs use the environment variables `TSP_EMAIL` and `TSP_API_TOKEN`
for credentials and do not have to passed on the command line.

#### Creating a Metric definition with Python Metric API

The following is example of defining a metric using the Python Metric API:

```
import tspapi

api = tspapi.API()

metric = api.metric_create(name='API_METRIC',
                           display_name='API Metric',
                           display_name_short='API Metric',
                           description='An API metric',
                           default_aggregate='avg',
                           default_resolution=1000,
                           unit='number',
                           _type='STOCK_PRICE')

print(metric)

```
running the script above outputs the following:
```

Metric(name='API_METRIC', display_name='API Metric', display_name_short='API Metric', description='An API metric', default_aggregate='AVG', default_resolution=1000, unit='number', _type='STOCK_PRICE', is_disabled='False')
```



### Measurement API

The heart of this course is the ability to use the Measurement API to get data into TrueSight
Intelligence.

#### Creating a Measurement with `curl`

```
curl https://$TSP_API_HOST/v1/measurements \
  -X POST                                  \
  -u "$TSP_EMAIL:$TSP_API_TOKEN"           \
  -H "Content-Type: application/json"      \
  -d '{
        "metric": "CPU",
        "source": "myserver",
        "measure": 2,
        "timestamp": 1377043134,
        "metadata": {
          "app_id": "Servers"
         }
      }'
```

#### Creating a Metric definition with `measurement-create`

You can generate a measurement using as CLI as shown here:

```
measurement-create -n CPU -m 0.8 -s 'myserver' -p app_id="LittleDog" -d 1461092253
```

which results in the following output if the measurement is successfully created:

```
{
    "result": {
        "success": true
    }
}
```

#### Creating a Measurements with the Python Measurement API

The following is example of defining a measurement using the Python Measurement API:
```
import tspapi

api = tspapi.API()

api.measurement_create(metric='CPU',
                       value=0.8,
                       source='my-server')
```

## Lab Exercise Background

This section describes a scenario in which business data is stored in a relation database
and we need to extract and send to TrueSight Intelligence. For this lab we are using the
[MariaDB](https://en.wikipedia.org/wiki/MariaDB) for our relation database which is a drop in replacement
for [MySQL](https://en.wikipedia.org/wiki/MySQL). When the virtual machine was created a `cron` jobs
was created that starts populating the database with simulated data.

### The Data

The data we are interested in is located in a table named `ol_transactions` the `app` database


```
MariaDB [app]> describe ol_transactions;
+----------+------------+------+-----+---------+----------------+
| Field    | Type       | Null | Key | Default | Extra          |
+----------+------------+------+-----+---------+----------------+
| id       | bigint(20) | NO   | PRI | NULL    | auto_increment |
| dt       | datetime   | NO   |     | NULL    |                |
| total    | bigint(20) | NO   |     | NULL    |                |
| duration | double     | NO   |     | NULL    |                |
+----------+------------+------+-----+---------+----------------+
```

### Viewing The Data


1. At the command line run the following:

     ```
     mysqldb
     ```

2. This will display the following prompt:

     ```
     [vagrant@tsi-lab-01 ~]$ mysqldb
     Reading table information for completion of table and column names
     You can turn off this feature to get a quicker startup with -A

     Welcome to the MariaDB monitor.  Commands end with ; or \g.
     Your MariaDB connection id is 129
     Server version: 5.5.47-MariaDB MariaDB Server

     Copyright (c) 2000, 2015, Oracle, MariaDB Corporation Ab and others.

     Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

     MariaDB [app]>

     ```

3. Run the following SQL query which limits the return rows to 10:

     ```
     MariaDB [app]> select * from ol_transactions limit 10;
     ```

4. Which will display output similar to below:

```
+----+---------------------+-------+----------+
| id | dt                  | total | duration |
+----+---------------------+-------+----------+
|  1 | 2016-04-18 17:26:00 |   726 |   407.31 |
|  2 | 2016-04-18 17:27:00 |   769 |   330.11 |
|  3 | 2016-04-18 17:28:00 |   529 |   460.87 |
|  4 | 2016-04-18 17:29:00 |   259 |   170.36 |
|  5 | 2016-04-18 17:30:00 |   703 |   277.52 |
|  6 | 2016-04-18 17:31:00 |   816 |   726.88 |
|  7 | 2016-04-18 17:32:00 |   465 |   150.15 |
|  8 | 2016-04-18 17:33:00 |    84 |   166.53 |
|  9 | 2016-04-18 17:34:00 |   624 |    228.7 |
| 10 | 2016-04-18 17:35:00 |   577 |   720.33 |
+----+---------------------+-------+----------+
10 rows in set (0.00 sec)
```

## Exercise 4-1 Defining Your Metrics

To run the script `labs\lab-4\ex-4-1.metrics.py`.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-4-1.metrics.py
    ```

## Exercise 4-2 Extracting Data From The Database Using SQL

To run the script `labs\lab-4\ex-4-2.metrics.py`.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-4-2.metrics.py
    ```

example output from running the script is shown here:

```
+---------------------+-------+----------+
| dt                  | total | duration |
+=====================+=======+==========+
| 2016-04-19 18:59:00 |   560 |    58.03 |
+---------------------+-------+----------+
| 2016-04-19 19:00:00 |   450 |   810.71 |
+---------------------+-------+----------+
| 2016-04-19 19:01:00 |   178 |   966.05 |
+---------------------+-------+----------+
| 2016-04-19 19:02:00 |   200 |   248.84 |
+---------------------+-------+----------+
| 2016-04-19 19:03:00 |   206 |    88.75 |
+---------------------+-------+----------+
...
```


## Exercise 4-3 Sending Extracted Data Using Measurement API

Run the script `labs\lab-4\ex-4-3.metrics.py`.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-4-3.metrics.py
    ```
