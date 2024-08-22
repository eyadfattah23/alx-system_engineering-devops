# Web stack debugging #4

Steps:

1. Booted the server knowing that the problem is the server can't handle many requests. I knew that because running the command `ab -c 100 -n 2000 localhost/` would result in `Failed requests: 943`

2. searched the problem on google and tried changing the **worker_processes** from 4 to 6

   > this resulted in decreasing failed requests --> `Failed requests: 17`

3. tried increasing **worker_processes** to more than 6 but this failed and `ab` just stops

4. searched more and found this link [Configuring Nginx to Handle 100 Thousands Request Per Minute](https://tecadmin.net/configuring-nginx-to-handle-100-thousands-request-per-minute/)

5. so tried Tuning worker connections to 1024, 2000 and other numbers but it didn't change much --> `Failed requests: 9`

6. added those lines to `/etc/sysctl.conf` then `sudo sysctl -p`:

```bash
# Increase the maximum number of file descriptors
fs.file-max = 2097152

# Increase the size of the connection backlog
net.core.somaxconn = 1024

# Increase the maximum number of incoming connections
net.ipv4.tcp_max_syn_backlog = 2048

# Decrease the time for TCP to enter TIME_WAIT state
net.ipv4.tcp_fin_timeout = 15

# Enable TCP Fast Open
net.ipv4.tcp_fastopen = 3

# Increase the available network buffers
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# Enable TCP window scaling
net.ipv4.tcp_window_scaling = 1
```

it didn't change much --> `Failed requests: 2` and sometimes `Failed requests: 1`

7. **_finally_** more searching and reading discord messages, found out this [blog] (https://shazaali.substack.com/p/0x1b-web-stack-debugging-4) by ShazaAly

8. changed the ulimit parameter from 15 to 2048 in `/etc/default/nginx`

```vim
# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 2048"

```

**and voila!**--> it works
