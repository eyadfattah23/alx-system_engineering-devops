# Web server

## Resources:

[log files in Ubuntu Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

[Method and Description](https://www.tutorialspoint.com/http/http_methods.htm)

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
