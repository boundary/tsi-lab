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

DROP FUNCTION IF EXISTS rand_amount;
DELIMITER //
CREATE FUNCTION rand_amount (max BIGINT, min BIGINT, divisor DOUBLE)
RETURNS DOUBLE DETERMINISTIC
RETURN ROUND(((FLOOR(RAND() * ((max - min) + 1)) + min)/divisor), 2);
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

DROP PROCEDURE IF EXISTS insert_activity_row;
DELIMITER //
CREATE PROCEDURE insert_activity_row(dt DATETIME, online BIGINT)
BEGIN
    INSERT INTO ol_activity(dt, online)
    VALUES(dt, online);
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_activity_data;
DELIMITER //
CREATE PROCEDURE insert_activity_data(dt DATETIME)
BEGIN
    CALL insert_activity_row(dt, rand_range(0, 1000));
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_transaction_row;
DELIMITER //
CREATE PROCEDURE insert_transaction_row(dt DATETIME, total BIGINT, duration DOUBLE)
BEGIN
    INSERT INTO ol_transactions(dt, total, duration)
    VALUES(dt, total, duration);
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_transaction_data;
DELIMITER //
CREATE PROCEDURE insert_transaction_data(dt DATETIME)
BEGIN
    CALL insert_transaction_row(dt, rand_range(0, 1000), rand_amount(30000, 1000000, 1000.0));
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_sales_row;
DELIMITER //
CREATE PROCEDURE insert_sales_row(dt DATETIME, region VARCHAR(32), category VARCHAR(32), amount DOUBLE, items BIGINT)
BEGIN
    INSERT INTO ol_sales(dt, category, region, amount, items)
    VALUES(dt, category, region, amount, items);
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_sales_data;
DELIMITER //
CREATE PROCEDURE insert_sales_data(dt DATETIME)
BEGIN
    DECLARE items BIGINT;

    SELECT rand_range(0, 1000) INTO items;
    CALL insert_sales_row(dt, 'north', 'appliances' , round(rand_amount(0, 10000, 1000.0) * items, 2), items);

    SELECT rand_range(0, 1000) INTO items;
    CALL insert_sales_row(dt, 'south', 'books'      , round(rand_amount(0, 10000, 1000.0) * items, 2), items);

    SELECT rand_range(0, 1000) INTO items;
    CALL insert_sales_row(dt, 'east' , 'clothing'   , round(rand_amount(0, 10000, 1000.0) * items, 2), items);

    SELECT rand_range(0, 1000) INTO items;
    CALL insert_sales_row(dt, 'west' , 'electronics', round(rand_amount(0, 10000, 1000.0) * items, 2), items);

END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_cart_data;
DELIMITER //
CREATE PROCEDURE insert_cart_data(dt DATETIME)
BEGIN
    INSERT INTO ol_cart(dt, amount, items)
    VALUES(dt, rand_amount(0, 1236156, 1000.0), rand_range(0, 1000));
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_business_data;
DELIMITER //
CREATE PROCEDURE insert_business_data(dt DATETIME)
BEGIN
    INSERT INTO business_metrics(dt, percent, duration, bytes)
    VALUES(dt, rand_range(0, 100)/100.0, rand_range(0, 1000), rand_range(0, 50000));
END
//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_data;
DELIMITER //
CREATE PROCEDURE insert_data()
BEGIN
  DECLARE dt DATETIME;
  SELECT round_to_minute(NOW()) INTO dt;

  CALL insert_activity_data(dt);
  CALL insert_business_data(dt);
  CALL insert_cart_data(dt);
  CALL insert_sales_data(dt);
  CALL insert_transaction_data(dt);
END
//
DELIMITER ;

