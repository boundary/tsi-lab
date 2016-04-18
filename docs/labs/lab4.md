Lab 4 - Metric and Measurement APIs
===================================

## Overview

This lab will introduce you to the Metric and Measurement APIs by showing you how to
extracting example business data from a MySQL database and sending the business data
to TrueSight Intelligence.

## Metrics versus Measurements

_Metrics_ and _Measurements_ are often used interchangeable by in the context of the TrueSight Intelligence APIs
we need to make a distinction as follows:

- *Metrics* are the *definition* of what the time series represents
- *Measurements* are the *actual* time series values that are collected

### Metric

A metric definitions consists of the following:

- Name
- Display Name
- Display Name Short
- Description
- Default Aggregate
- Default Resolution
- Type
- Units

#### Name

This is the primary key and is used to uniquely identify each metric in an account. The name is all
uppercase with addition of underscores(`_`) and periods('.'). Some of the built-in metrics include:
CPU, Network In, or Data Disk Out.

#### Display Name

Label to identify the metric in the user interface or other place where user readable text is needed.

#### Display Name Short

Same use as _Display Name_ but in those cases where shortened text is required (limit to 20 characters).

#### Description

Provides textual information or other information relevant in describing the metric.

#### Default Aggregate

When graphing the metric that makes the most sense, which is one of:

- Average
- Minimum
- Maximum
- Sum

#### Type

**TODO** What is the type user for in TrueSight Intelligence?

#### Unit

This field consists of an enumerated type the describes the unit of meaurement of the metric. The types
consist of the following;

- ByteCount
- Duration
- Number
- Percent

_NOTE_: _Duration_ is milliseconds and is not current configurable. Percent is given in decimal form, for
example %63.2 would be given as 0.632.

### Measurements

Are the time series data collected for a particular _metric_ which are made of the following:

- Metric
- Value
- Source
- Timestamp

#### Metric

Refers to the specific _Metric_ of the Measurement

#### Value

Value of the metric at the given timestamp. If the Metric unit is _percent_ then this is value in its
decimal equivalent.

#### Source

Most often the system hostname but it is used to indicate the specific instance of the thing being measured. For
example if were measuring individual utilization for CPU cores the source would refer to the specific core.

#### Timestamp

When the measurement occurred in [UNIX epoch time](https://en.wikipedia.org/wiki/Unix_time) which is either
in seconds or milliseconds.

#### Measurement Properties

In addition to the previously discussed Measurement fields, there are optional fields for further
classification of a measurement.

**TO BE DISCUSSED**

### Metric API


### Measurement API

## Example Background

### MariaDB Database

The MariaDB is a equivalent database of MySQL

### Database Schema

```
MariaDB [app]> show tables;
+------------------+
| Tables_in_app    |
+------------------+
| business_metrics |
| ol_activity      |
| ol_cart          |
| ol_sales         |
| ol_transactions  |
+------------------+
5 rows in set (0.00 sec)

MariaDB [app]>
```

```
CREATE TABLE ol_activity
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  dt DATETIME NOT NULL,
  online BIGINT NOT NULL
);
```

### Running MariaDB Queries


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

3. Run the following:

     ```
     MariaDB [app]> select now();
     ```

4. Which will display output similiar to below:

```
MariaDB [app]> select now();
+---------------------+
| now()               |
+---------------------+
| 2016-04-18 14:27:47 |
+---------------------+
1 row in set (0.00 sec)
```


## Exercise 4-1 Defining Your Metrics

Run the script `labs\lab-4\ex-4-1.metrics.py`.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-4-1.metrics.py
    ```

## Exercise 4-2 Extracting Data From The Database Using SQL

Run the script `labs\lab-4\ex-4-2.metrics.py`.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-4-2.metrics.py
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
