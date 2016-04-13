Lab 5 - Logfile to API
======================

## Overview

This lab will introduce to parsing an Apache HTTP log to extract measurements that are then sent to
the measurement APIs


## Apache Web Server Introduction



## Exercise 5-1 - Parsing an Apache Log File

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

