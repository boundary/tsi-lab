#!/usr/bin/env python
import pymysql
import os
import syslog

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db = os.environ['DB_DATABASE']

syslog.openlog(logoption=(syslog.LOG_PID|syslog.LOG_INFO), facility=syslog.LOG_USER)
syslog.syslog("Inserting new business data into database.")

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'CALL insert_data()'
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()
