#!/usr/bin/env python
#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import syslog
import time

import petl
import pymysql
import tspapi
from tspapi import Measurement
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

        # Set our application id from the environment variable
        self.app_id = os.environ['TSI_APP_ID']

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
        syslog.syslog(str(message))
        print(message)

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
            sql = "select min(dt) as min_dt from ol_transactions where dt >= '{0}'".format(last)

        self.log("SQL: {0}".format(sql))
        table = petl.fromdb(self.connection, sql)
        extract_dt = petl.values(table, 'min_dt')[0]
        return extract_dt

    def get_data(self, min_dt, max_dt):
        sql = "select dt, total, duration from ol_transactions where dt > '{0}' and dt <= '{1}'".format(min_dt, max_dt)
        self.log("SQL: {0}".format(sql))
        self.table = petl.fromdb(self.connection, sql)

    def process_records(self):
        rows = petl.values(self.table, 'dt', 'total', 'duration')
        row_count = 0
        measurements = []
        properties = {'app_id': self.app_id}
        print(rows)
        # self.log("process_records")
        for row in rows:
            timestamp = int(row[0].strftime('%s'))
            total = int(row[1])
            duration = int(row[2])
            self.log("Add Measurements => dt: {0}, total: {1}, duration: {2} ".format(timestamp, total, duration))
            row_count += 1
            # self.log("Row Count {0}".format(row_count))
            time.sleep(.01)
            if row_count == 10:
                # send measurements
                self.log("Sending {0} measurements".format(row_count))
                self.log(measurements)
                self.api.measurement_create_batch(measurements)
                measurements = []
                row_count = 0
            else:
                measurements.append(Measurement(metric='ONLINE_TRANSACTION_COUNT',
                                                source='FOO',
                                                value=total))
                measurements.append(Measurement(metric='ONLINE_TRANSACTION_TIME',
                                                source='FOO',
                                                value=duration))

    def process_data(self):
        last_record = self.get_last_fetched_record()

        max_dt = self.get_max_dt()
        min_dt = self.get_min_dt(last_record)
        self.get_data(min_dt, max_dt)
        self.process_records()

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
