#!/usr/bin/env python
import pymysql

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

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM business_metrics ORDER BY dt DESC"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
