#!/usr/bin/env python
import pymysql
import os

host = os.environ['DB_HOST']
host = os.environ['DB_USER']
host = os.environ['DB_PASSWORD']
host = os.environ['DB_DATABASE']

connection = pymysql.connect(host='localhost',
                             user='admin',
                             password='admin123',
                             db='app',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "CALL insert_data({0})".format(1)
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()
