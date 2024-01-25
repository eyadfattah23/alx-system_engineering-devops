create user if not exists 'replica_user'@'%';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

grant select on mysql.user to 'holberton_user'@'localhost';
