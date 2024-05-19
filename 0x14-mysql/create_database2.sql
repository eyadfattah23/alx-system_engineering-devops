-- create database on WEB-01 only to test replication
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6
(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6
VALUES (1,'EDDY');
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
