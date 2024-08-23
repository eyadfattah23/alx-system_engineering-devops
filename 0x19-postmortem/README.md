# Postmortem

<div align="center">
<img src="https://media.giphy.com/media/3ohc0Tl6T6UxpboOha/giphy.gif" align="center" style="width: 100%" />
</div>

## Issue Summary:

- **Duration**: 10 hrs, Start time: Aug 22, 2024 1:00 PM (GMT+03:00),- End time: Aug 22, 2024 11:00 PM (GMT+03:00)

- **Impact**: The community section in our website was down, Users using our online community where they can post, comment and read posts were getting failed request or 502 bad getaway errors, 30-35% of the users were affected.

- **Root** **cause**: The number of files/resources that the webserver(nginx) could open simultaneously were only 15 files at a time this, value is determined by `ULIMIT` parameter in a file of path `/etc/default/nginx`

## Timeline:

- **Aug 22, 2024 1:00 PM (GMT+03:00)** - Issue was detected. Many customers complained to the customer service and the monitoring service notified us about having a huge load on the server

- **Actions taken:** The sys-admin team began investigating then supposed the problem was in the maximum number of simultaneous connections that can be opened by a worker process was too low.

- **Misleading Investigation:** The focus on those 2 parameters (worker connections and worker processes) fixed some of the problem but still 2-3% of the requests were failing.

- **Escalation:** **Aug 22, 2024 4:00 PM (GMT+03:00)** - The incident was escalated to the Back-end team thinking the problem was in the database.

- **Aug 22, 2024 6:00 PM (GMT+03:00)** - back-end team responded with "no issue with the data base"

- **Aug 22, 2024 9:00 PM (GMT+03:00)** - After further investigations by the sys-admin team the discovered that the problem was the low number of files that the ngnix web server could do processes on.

## Root cause and resolution:

### Steps by the sys-admin team:

1. Booted the server knowing that the problem is the server can't handle many requests. They knew that because running the command `ab -c 100 -n 2000 localhost/` would result in `Failed requests: 943`

2. searched the problem on google and tried changing the **worker_processes** from 4 to 6

   > this resulted in decreasing failed requests --> `Failed requests: 17`

3. tried increasing **worker_processes** to more than 6 but this failed and `ab` just stops.

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

#### **and voila!**--> it works, running `ab -c 100 -n 2000 localhost/` shows `Failed requests: 0` and the problem was the number of files that could be read by nginx simultaneously and is adjusted by the parameter "ULIMIT"

### Corrective and preventative measures

- Implement better load balancing to handle traffic efficiently.

- Improve server scaling strategies for sudden traffic spikes.

- More monitoring for web server performance.

- After adding a new feature or noticing change in the traffic on the website do a benchmarking test with a number of requests more than the expected number of requests by the users so that we handle traffic spikes.
