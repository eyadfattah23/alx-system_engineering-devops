# Web server

## Resources:

[log files in Ubuntu Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

[Method and Description](https://www.tutorialspoint.com/http/http_methods.htm)

[The NGINX Crash Course](https://www.youtube.com/watch?v=7VAI73roXaY&t=482s)

> ---> summary:
> S.N. Method and Description

    1 GET

    The GET method is used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.

    2 HEAD

    Same as GET, but transfers the status line and header section only.

    3 POST

    A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.

    4 PUT

    Replaces all current representations of the target resource with the uploaded content.

    5 DELETE

    Removes all current representations of the target resource given by a URI.

    6 CONNECT

    Establishes a tunnel to the server identified by a given URI.

    7 OPTIONS

    Describes the communication options for the target resource.

    8 TRACE

    Performs a message loop-back test along the path to the target resource.

[Domains, subdomains and paths](https://landingi.com/help/domains-vs-subdomains/)

[How To Set Up Nginx Server Blocks (Virtual Hosts) on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)

[How to Use SCP Command to Securely Transfer Files](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

## Learning Objectives

### General

    What is the main role of a web server
    What is a child process
    Why web servers usually have a parent process and child processes
    What are the main HTTP requests

### DNS

    What DNS stands for
    What is DNS main role

### DNS Record Types

    A
    CNAME
    TXT
    MX

```bash
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:

    remotely execute the ls ~/ command via ssh to see what ~/ contains
    create a file named some_page.html
    execute my 0-transfer_file script
    remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred

**Maarten’s PRO-tip:** When you use sudo su on your web-01 you can become root like this to test your file:

```bash
sylvain@ubuntu$ sudo su
root@ubuntu#
```

```nginx
user       www www;  ## Default: nobody
worker_processes  5;  ## Default: 1
error_log  logs/error.log;
pid        logs/nginx.pid;
worker_rlimit_nofile 8192;

events {
  worker_connections  4096;  ## Default: 1024
}

http {
  include    conf/mime.types;
  include    /etc/nginx/proxy.conf;
  include    /etc/nginx/fastcgi.conf;
  index    index.html index.htm index.php;

  default_type application/octet-stream;
  log_format   main '$remote_addr - $remote_user [$time_local]  $status '
    '"$request" $body_bytes_sent "$http_referer" '
    '"$http_user_agent" "$http_x_forwarded_for"';
  access_log   logs/access.log  main;
  sendfile     on;
  tcp_nopush   on;
  server_names_hash_bucket_size 128; # this seems to be required for some vhosts

  server { # php/fastcgi
    listen       80;
    server_name  domain1.com www.domain1.com;
    access_log   logs/domain1.access.log  main;
    root         html;

    location ~ \.php$ {
      fastcgi_pass   127.0.0.1:1025;
    }
  }

  server { # simple reverse-proxy
    listen       80;
    server_name  domain2.com www.domain2.com;
    access_log   logs/domain2.access.log  main;

    # serve static files
    location ~ ^/(images|javascript|js|css|flash|media|static)/  {
      root    /var/www/virtual/big.server.com/htdocs;
      expires 30d;
    }

    # pass requests for dynamic content to rails/turbogears/zope, et al
    location / {
      proxy_pass      http://127.0.0.1:8080;
    }
  }

  upstream big_server_com {
    server 127.0.0.3:8000 weight=5;
    server 127.0.0.3:8001 weight=5;
    server 192.168.0.1:8000;
    server 192.168.0.1:8001;
  }

  server { # simple load balancing
    listen          80;
    server_name     big.server.com;
    access_log      logs/big.server.access.log main;

    location / {
      proxy_pass      http://big_server_com;
    }
  }
}
```

---

To configure your DNS records with an A (Address) entry to point your root domain to the IP address of your web server (web-01), you'll need to do the following:

    Access Your DNS Provider:
    Log in to the website of your DNS hosting provider. This is typically the service where you purchased your domain.

    Locate DNS Management or DNS Settings:
    Look for a section called "DNS Management," "DNS Settings," or something similar. This is where you can configure your domain's DNS records.

    Find the A Record Section:
    Locate the section for A (Address) records. This is where you can map your domain to an IP address.

    Add or Edit the A Record:

        If there is an existing A record for your domain, edit it to set the IP address to your web server (web-01).

        If there isn't an A record, add a new one. The A record should look something like this:

        Type: A
        Name: @ (represents the root domain)
        Value: IP Address of web-01


    If your DNS provider requires a fully qualified domain name (FQDN) in the "Name" field, you can use your root domain (e.g., example.com) instead of @.

    Save Changes:
    Save your changes. DNS changes may take some time to propagate across the internet, so it might not take effect immediately.

Here's a simple example:

    Type: A
    Name: @ (or your root domain if required)
    Value: IP Address of web-01

Remember that DNS changes can take some time to propagate, and during this period, users might still see the old information cached by their ISPs or browsers.
