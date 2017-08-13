-- creates database and user
-- grants all priveleges for database hbnb_dev_db
-- grants select priveleges to database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER 'hbnb_test'@'localhost'; -- reference bug, must drop and flush before create user
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVELEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema. * TO 'hbnb_test'@'localhost';
