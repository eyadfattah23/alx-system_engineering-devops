-- create a new user for the replica server.

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
