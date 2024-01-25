CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS 'nexus6' 
(id int, name varchar(255));
INSERT INTO nexus6
VALUES (1,'EDDY');

GRANT SELECT ON `tyrell_corp`.* TO `holberton_user`@`localhost`;
