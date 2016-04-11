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

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db = os.environ['DB_DATABASE']

syslog.openlog(facility=syslog.LOG_USER)
syslog.syslog("Inserting new business data into database.")

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "CALL extract_data()"
        cursor.execute("SELECT dt, percent, duration, bytes FROM business_metrics")

        for row in cursor.fetchall():
            print("{0}, {1}, {2}, {3}".format(row['dt'], row['percent'], row['duration'], row['bytes']))


finally:
    connection.close()
