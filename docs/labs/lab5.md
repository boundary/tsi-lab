Lab 5 - Logfile to API
======================

## Overview

This lab will introduce to parsing an Apache HTTP log to extract measurements that are then sent to
the measurement APIs


## Apache Web Server Introduction

The [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server) has a long history with
its initial release in 1995. The Apache HTTP Server is descendant of the
[NCSA HTTPd Server](https://en.wikipedia.org/wiki/NCSA_HTTPd) and was started when development on the
NCSA HTTPd Server stalled.

A key feature of the Apache Web Server is the ability to log received requests to a log file of
your choosing and format. The out of the box file is named `access_log` and on RHEL/Centos platforms
the path to the file is `/var/log/httpd/access_log`. The default format of the log file is referred to
as `combined`. Information about received requests are continuously appended to the log file.

To extract useful content from the log file at we need to perform the following:

1. Continuously read the log file looking for new requests appended to the log.
2. For each line parse the content knowing the format of each line or record.
3. Extract the content of interest by filtering and searching each line or record.
4. Send the extract content to TrueSight Intelligence using the Measurement API.


## Exercise 5-1 - Getting Updates From A Log File

A useful unix untility [`tail`](https://en.wikipedia.org/wiki/Tail_(Unix)) permits the monitoring of a log
file and outputs new lines or records as they are written to the file. An example of using this utility is shown
here:

```
$ tail -f /var/log/cron
```
which is a log that shows [`cron`] jobs that have been executed by the system.

For this exercise we will introduce the same capability by in Python code.


1. Change directory to `labs/lab-5`

     ```
     $ cd labs/lab-5
     ```

2. Run the following command:

    ```
    $ ex5-1.log.py access_log
    ```

## Exercise 5-2 - Reading the live Apache Log File

1. Run the following command:
    ```
    $ sudo ex5-2.log.py /var/log/httpd/access_log
    ```

## Exercise 5-3 - Reading live Apache Log Files and Sending Measurements

1. Run the following command:
    ```
    $ sudo ex5-3.log.py /var/log/httpd/access_log
    ```

