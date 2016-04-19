#!/usr/bin/env python
# import petl as etl
# import pymysql
# connection = pymysql.connect(user='admin', password='admin123', database='app')
# table = etl.fromdb(connection, 'SELECT * FROM business_metrics')
# print(table.look())
# sorted = etl.sort(table, 'dt');
# print(sorted.look())

import logging
import syslog
import time

import petl
import pymysql
import tspapi
import filelock

import os


class ETL(object):
    def __init__(self, lock_file_path=None, last_record_path=None):
        """
            1) Open the syslog for writing
            2) Allocate an instance of API class
            3) Set defaults on member variables
        :return:
        """
        syslog.openlog(logoption=(syslog.LOG_PID | syslog.LOG_INFO), facility=syslog.LOG_USER)
        logging.basicConfig(level=logging.DEBUG)
        self.api = tspapi.API()

        if lock_file_path is not None:
            self.lock_file_path = lock_file_path
        else:
            raise ValueError("Lock file path not specified")

        if last_record_path is not None:
            self.last_record_path = last_record_path
        else:
            raise ValueError("Lock file path not specified")

        self.host = None
        self.user = None
        self.password = None
        self.database = None
        self.connection = None
        self.table = None

        self.get_db_config()

    def log(self, message):
        """
        Wrapper method for writing to logging and syslog

        :param message:
        :return:
        """
        logging.debug(message)
        syslog.syslog(message)

    def get_db_config(self):
        """
        Extract database configuration from environment variables
        :return:
        """
        self.host = os.environ['DB_HOST']
        self.user = os.environ['DB_USER']
        self.password = os.environ['DB_PASSWORD']
        self.database = os.environ['DB_DATABASE']

    def db_connect(self):
        """
        Open connection to the database
        :return:
        """
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.database)

    def db_close(self):
        """
        Close connection to the database
        :return:
        """
        self.connection.close()

    def fetch_records(self, last):
        sql = "SELECT dt, online FROM ol_activity WHERE dt >= '{0}'".format(last)
        table = petl.fromdb(self.connection, sql)
        print(table)
        petl.look(table)


    def acquire_lock(self):
        self.log("Acquiring lock file from {0}".format(self.lock_file_path))
        return filelock.FileLock(self.lock_file_path)

    def get(self):
        """
        Reads data from last record file, creates if it does not exist
        :return:
        """
        data = None
        try:
            with open(self.last_record_path, 'rat') as f:
                data = f.read()
                self.log("data: {0}".format(data))
        except IOError as e:
            self.log(e.message)

        return data

    def put(self, data):
        """
        Writes data to last record file
        :param data:
        :return:
        """
        with open(self.last_record_path, 'wt') as f:
            self.log("data: {0}".format(data))
            f.write(str(data))

    def get_last_fetched_record(self):
        data = self.get()
        if data is None or len(data) == 0:
            last = None
        else:
            last = data
        return last

    def set_last_fetched_record(self, last):
        self.put(last)

    def get_max_dt(self):
        """
        Gets the current maximum date in the table
        :return:
        """
        sql = 'select max(dt) as max_dt from ol_transactions'
        self.log("SQL: {0}".format(sql))
        table = petl.fromdb(self.connection, sql)
        max_dt = petl.values(table, 'max_dt')[0]
        return max_dt

    def get_min_dt(self, last):
        """
        Gets the minimum date considering previous extractions from the table.
        :param last:
        :return:
        """
        if last is None or len(last) == 0:
            sql = "select min(dt) as min_dt from ol_transactions"
        else:
            print("last: ".format(last))
            sql = "select min(dt) as min_dt from ol_transactions where dt >= '{0}'".format(last)

        self.log("SQL: {0}".format(sql))
        table = petl.fromdb(self.connection, sql)
        extract_dt = petl.values(table, 'min_dt')[0]
        return extract_dt

    def get_data(self, min_dt, max_dt):
        sql = "select * from ol_transactions where dt > '{0}' and dt <= '{1}'".format(min_dt, max_dt)
        self.log("SQL: {0}".format(sql))
        self.table = petl.fromdb(self.connection, sql)

    def process_records(self):
        self.table = petl.fromdb(self.connection, sql)
        print(self.table)

    def process_data(self):
        last_record = self.get_last_fetched_record()

        max_dt = self.get_max_dt()
        min_dt = self.get_min_dt(last_record)
        self.get_data(min_dt, max_dt)

        self.set_last_fetched_record(max_dt)

    def run(self):
        """
        1) Acquire lock
        2) Connect to the database
        3) Look for data to process
        4) If data available then process
        :return:
        """
        lock = self.acquire_lock()
        try:
            with lock.acquire(timeout=0):
                self.log('acquired lock')
                self.db_connect()
                self.process_data()
        except filelock.Timeout:
            self.log('Extraction process running skipping')

if __name__ == '__main__':
    etl = ETL(lock_file_path='etl.lock',
              last_record_path='etl.last')
    etl.run()
