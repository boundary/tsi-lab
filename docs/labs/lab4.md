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

### MySQL Database

### Database Schema


## Exercise 4-1 Defining Your Metrics


## Exercise 4-2 Extracting Data From The Database Using SQL


## Exercise 4-3 Sending Extracted Data Using Measurement API
