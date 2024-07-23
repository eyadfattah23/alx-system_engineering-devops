# Setting MySQL on my servers

## to add a public ssh hey:

1. run `vi /home/cloud-user/.ssh/authorized_keys`
2. Paste your public key from the new line
3. Save changes by `:x` and Enter

## Install mysql 5.7

1. Copy the key here to your clipboard

https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html

2. Save it in a file on your machine i.e. signature.key and then

`sudo apt-key add signature.key`

3. add the apt repo

`sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'`

3. update apt

`sudo apt-get update`

4. now check your available versions:

```bash
vagrant@ubuntu-focal:/vagrant$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```

5. Now install mysql 5.7

`sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7\*`

---

## Resources:

**https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql#step-1-adjusting-your-source-server-s-firewall**

**https://stackoverflow.com/questions/18498359/creating-tar-file-and-naming-by-current-date**

### new commands used in web01

`ssh-keygen -t rsa -b 4096`

`ssh-copy-id ubuntu@100.25.162.125`

`sudo mysqldump -u root tyrell_corp > tyrell_corp.sql`

`scp tyrell_corp.sql ubuntu@100.25.162.125:/tmp/`

`sudo mysql tyrell_corp < /tmp/tyrell_corp.sql`

### new mysql commands used in web02

CHANGE MASTER TO
MASTER_HOST='52.91.152.150',
MASTER_USER='replica_user',
MASTER_PASSWORD='password',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;

## to execute a sql script:

`cat file.sql | sudo mysql -h localhost -u user(root) -p password`

Using % as the hostname is a wildcard that allows the user to connect from any host. This is particularly useful when you want to grant access to a user regardless of the IP address they are connecting from.

Here's a more detailed breakdown:
Hostname in MySQL User Accounts

When you create a user in MySQL, you specify both the username and the hostname. For example, a user user1 connecting from localhost would be specified as:

```sql

'user1'@'localhost'
```

Using % as a Wildcard

The % character is a wildcard in MySQL, which matches any string of zero or more characters. When used in the hostname part, it allows the user to connect from any host. For example:

```sql

'user1'@'%'
```

### TO Migrate Data to replicas:

1. `ssh ubuntu@source_server_ip`
2. `sudo mysqldump -u root db > db.sql`
3. from another window on the same server run mysql then `UNLOCK TABLES;` then exit mysql

---

4. SSH into the replica server `ssh ubuntu@replica_server_ip`

5. `sudo mysql` then `CREATE DATABASE db;` then exit from it

6. `sudo mysql db < /tmp/db.sql`
