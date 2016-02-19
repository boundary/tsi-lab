#!/usr/bin/env python

import petl as etl
import pymysql
connection = pymysql.connect(user='admin', password='admin123', database='app')
table = etl.fromdb(connection, 'SELECT * FROM business_metrics')
print(table.look())
sorted = etl.sort(table, 'dt');
print(sorted.look())
