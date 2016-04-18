-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile
USE app;

DROP FUNCTION IF EXISTS rand_range;
DELIMITER //
CREATE FUNCTION rand_range (max BIGINT, min BIGINT)
RETURNS DOUBLE DETERMINISTIC
RETURN FLOOR(RAND() * ((max - min) + 1)) + min;
//
DELIMITER ;

DROP FUNCTION IF EXISTS round_to_minute;
DELIMITER //
CREATE FUNCTION round_to_minute (dt DATETIME)
RETURNS DATETIME DETERMINISTIC
RETURN CONVERT(DATE_FORMAT(dt,'%Y-%m-%d-%H:%i:00'), DATETIME);
//
DELIMITER ;


DROP TABLE IF EXISTS business_metrics;
CREATE TABLE business_metrics
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT "Row identifier",
  dt DATETIME NOT NULL,
  percent DOUBLE NOT NULL,
  duration BIGINT NOT NULL,
  bytes BIGINT NOT NULL
);

DROP TABLE IF EXISTS ol_activity;
CREATE TABLE ol_activity
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  dt DATETIME NOT NULL,
  online BIGINT NOT NULL
);

DROP TABLE IF EXISTS ol_transactions;
CREATE TABLE ol_transactions
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  dt DATETIME NOT NULL,
  total BIGINT NOT NULL,
  duration DOUBLE NOT NULL
);

DROP TABLE IF EXISTS ol_sales;
CREATE TABLE ol_sales
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  dt DATETIME NOT NULL,
  category VARCHAR(32) NOT NULL,
  region VARCHAR(32) NOT NULL,
  amount DOUBLE NOT NULL,
  items DOUBLE NOT NULL
);

DROP TABLE IF EXISTS ol_cart;
CREATE TABLE ol_cart
(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  dt DATETIME NOT NULL,
  amount DOUBLE NOT NULL,
  items BIGINT NOT NULL
);

DROP PROCEDURE IF EXISTS insert_cart_data;
DELIMITER //
CREATE PROCEDURE insert_cart_data(start_dt DATETIME, nrows BIGINT)
BEGIN
    INSERT INTO ol_cart(dt, amount, items)
    VALUES(date_add(start_dt, interval nrows minute), round(rand_range(0, 1236156)/1000.0, 2), rand_range(0, 1000));
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_data;
DELIMITER //
CREATE PROCEDURE insert_data(nrows BIGINT)
BEGIN
  DECLARE start_dt DATETIME;
  SELECT round_to_minute(NOW()) INTO start_dt;
  WHILE nrows > 0 DO
    INSERT INTO business_metrics(dt, percent, duration, bytes)
    VALUES(date_add(start_dt, interval nrows minute), rand_range(0, 100)/100.0, rand_range(0, 1000), rand_range(0, 50000));
    CALL insert_cart_data(start_dt, nrows);
    SET nrows = nrows - 1;
  END WHILE;
END
//
DELIMITER ; 


CALL insert_data(10);
