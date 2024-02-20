# Webstack monitoring

## General:

- The two main areas of monitoring are:

  1.  Performance Monitoring: This involves tracking various performance metrics of systems, networks, applications, and services. It includes monitoring CPU usage, memory usage, disk I/O, network bandwidth, response times, and other relevant performance indicators to ensure optimal system operation.

  2.  Security Monitoring: This involves monitoring for security-related events, anomalies, and threats within an organization's IT infrastructure. It includes monitoring for unauthorized access attempts, malware infections, data breaches, suspicious network traffic, and other security incidents to protect against potential security threats.

- Access logs for a web server (such as Nginx) contain records of all requests made to the server, including details such as the requesting IP address, requested URL, HTTP status code, user agent, and timestamp. These logs provide valuable insights into the traffic patterns, visitor demographics, and usage trends of the web server.

- Error logs for a web server (such as Nginx) contain records of errors and warnings encountered during the server's operation. This includes errors related to server configuration, HTTP errors (e.g., 404 Not Found), internal server errors (e.g., 500 Internal Server Error), and other issues that may affect the server's functionality or performance. Error logs help administrators diagnose and troubleshoot issues to ensure the smooth operation of the web server.

## steps_made:

1. Sign up for Datadog - using the US website of Datagog (https://app.datadoghq.com) and Use the US1 region
2. Install datadog-agent on web-01
3. Create an application key (type it in the search bar)
4. Copy-paste in Intranet user profile your DataDog API key (the one in the installing command) and DataDog application key.
5. look at the [metrics](https://intranet.alxswe.com/rltoken/4RPOEVDTqKXuvyU4Gkj2Bw)
6. go to https://app.datadoghq.com/monitors/create/metric
7. copy `system.io.w_s` or `system.io.r_s` and paste it in {Define the metric -> source -> Define the monitor’s query}
8. Set alert conditions:
   Trigger when the evaluated value is
   the threshold
   Alert threshold: > 100
   Warning threshold: > 90

9. in {Notify your team -> edit -> Monitor Name} type `avg(last5m):avg:system.io.r_s{*}` or `avg(last5m):avg:system.io.w_s{*}`

10. in {Notify your team -> edit -> Monitor message} `system.io.w_s` or `system.io.r_s`

11. and press create

12. create dashboard with 4 gadgets

https://app.datadoghq.com/dashboard/5m4-vn5-48p?refresh_mode=sliding&from_ts=1708439916756&to_ts=1708443516756&live=true
