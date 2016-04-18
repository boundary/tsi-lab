#!/usr/bin/env python
# import petl as etl
# import pymysql
# connection = pymysql.connect(user='admin', password='admin123', database='app')
# table = etl.fromdb(connection, 'SELECT * FROM business_metrics')
# print(table.look())
# sorted = etl.sort(table, 'dt');
# print(sorted.look())

import pymysql
import os
import syslog
import petl as etl
import tspapi

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db = os.environ['DB_DATABASE']

api = tsapi.API()

syslog.openlog(logoption=(syslog.LOG_PID|syslog.LOG_INFO), facility=syslog.LOG_USER)
syslog.syslog("Extracting business metrics from database")

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db)


sql = "SELECT dt, online FROM ol_activity WHERE dt >= '{0}'".format('2016-01-01')

table = etl.fromdb(connection, 'SELECT dt, online FROM ol_activity')
print(table)

etl.look(table)

connection.close()
