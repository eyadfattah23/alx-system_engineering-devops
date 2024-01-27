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

### new commands used in web01

ssh-keygen -t rsa -b 4096
ssh-copy-id ubuntu@100.25.162.125
sudo mysqldump -u root tyrell_corp > tyrell_corp.sql
scp tyrell_corp.sql ubuntu@100.25.162.125:/tmp/
sudo mysql tyrell_corp < /tmp/tyrell_corp.sql

### new mysql commands used in web02

CHANGE MASTER TO
MASTER_HOST='100.25.22.31',
MASTER_USER='replica_user',
MASTER_PASSWORD='password',
MASTER_LOG_FILE='mysql-bin.000329',
MASTER_LOG_POS=154;
