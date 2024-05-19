-- script that creates the MySQL server user holberton_user
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
GRANT SELECT ON `tyrell_corp`.* TO `holberton_user`@`localhost`;
