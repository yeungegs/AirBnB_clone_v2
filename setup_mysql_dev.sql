-- creates database and user
-- grants all priveleges for database hbnb_dev_db
-- grants select priveleges to database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVELEGES ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema. * TO 'hbnb_dev'@'localhost';
