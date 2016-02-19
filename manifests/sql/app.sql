USE app;

DROP FUNCTION IF EXISTS rand_range;

DELIMITER //
CREATE FUNCTION rand_range (max BIGINT, min BIGINT)
RETURNS DOUBLE DETERMINISTIC
RETURN FLOOR(RAND() * ((max - min) + 1)) + min;
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

DROP PROCEDURE IF EXISTS insert_data;
DELIMITER //
CREATE PROCEDURE insert_data(nrows BIGINT)
BEGIN
  DECLARE start DATETIME;
  SELECT NOW() INTO start;
  WHILE nrows > 0 DO
    INSERT INTO business_metrics(dt, percent, duration, bytes)
    VALUES(date_add(start, interval nrows minute), rand_range(0, 100)/100.0, rand_range(0, 1000), rand_range(0, 50000));
    SET nrows = nrows - 1;
  END WHILE;
END
//
DELIMITER ; 


CALL insert_data(10);
