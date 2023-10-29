design: https://imgur.com/a/oO65E2g

# In this design a new server and a load balancer were added

we had in the previous design 3 major problems which were

> the server was a SPOF

> Downtime when maintenance needed

> Cannot scale if too much incoming traffic

### now after adding additional elements:

> it's ok if on of the servers fails because the other will work and the whole system won't fail

> If they need maintenance the downtime won't be a problem because the other server will handle the traffic however it will struggle with much traffic

> Now it will scale better if the servers have alot of traffic with double the speed as there are 2 servers now working to split the work.

> When multiple instances of identical server components are available, client requests to these components can be load balanced to ensure that the instances have roughly the same workload.

### distribution algorithm load balancer is configured:

> it works with Round Roben algorithm which handle the traffic by just circling around the servers giving them each a request by order. Let's say we have five requests named 1,2,3 and 4 server A will take request 1 then server B will take request 2 then server A will take request 3 then server A will take request 4 and so on with this algorithm even with more requests and servers

### Active-Active and Active-Passive:

#### 1-Active-Active:

    In an Active-Active setup, all nodes or instances are actively processing requests or providing services simultaneously. Each node shares the load and is responsible for a portion of the overall workload. This configuration is often used to distribute traffic across multiple resources to maximize performance and resource utilization.

#### 2-Active-Passive:

    In an Active-Passive setup, one node or instance (the "active" node) is actively processing requests or providing services, while the other node or nodes (the "passive" nodes) remain in standby mode. The passive nodes only become active if the primary node fails.

**this design uses active-active to maximize resource utilization and performance by distributing the load across multiple active nodes.**

### How a database Primary-Replica (Master-Slave) cluster works:

    The primary server handles write operations and maintains the authoritative copy of the data, while replica servers maintain read-only copies that can be used for read scaling and backup. Failover mechanisms ensure that the system can continue to operate in the event of a primary server failure. Data consistency and replication mechanisms are crucial to the success of this setup.

### the difference between the Primary node and the Replica node:

#### Primary (Master) Server:

    The primary server is the authoritative source of data and handles both read and write operations.
    All write operations, such as INSERT, UPDATE, and DELETE queries, are executed on the primary server.
    The primary server maintains the "master" copy of the data.

#### Replica (Slave) Servers:

    Replica servers are read-only copies of the data from the primary server.
    Replicas replicate data from the primary server to ensure they stay in sync.
    Read queries, like SELECT operations, can be distributed to replica servers, reducing the read load on the primary server and improving read performance.
    Replicas can also serve as a backup in case the primary server fails.

## Issues

> **SPOF(Single Point Of Failure)**: The single point of failure in this infrastructure is having only one load balancer

> **Security issues(no firewall, no HTTPS)**: The security issues are: a. The application communicate over unsecure HTTP protocol which might give attackers a chance to double cross sensitive data being transmitted bec. The application doesn’t have a firewall, This can allow an attacker to perform a denial of service attack(DOS or DDOS) that may cause a major downtime in the system, or allow a malicious attacker to breach the system exploiting unknown open ports.

> **No monitoring**:

Delayed Issue Detection:

Issues and anomalies within your systems can go undetected for extended periods. This means you may not become aware of problems until they have already caused disruptions or damage.

Difficulty in Troubleshooting:

When issues do occur, troubleshooting becomes more challenging and time-consuming without monitoring data to help identify the root causes.

Security Vulnerabilities:

Security breaches and vulnerabilities may remain undetected for longer, increasing the risk of data breaches and unauthorized access. Monitoring is crucial for identifying and responding to security threats.

Lack of Visibility:

Without monitoring, you have limited visibility into what is happening within your systems and infrastructure. You won't know if there are performance bottlenecks, security threats, or resource issues that require attention.

Unpredictable Maintenance:

Without monitoring, maintenance activities can be unpredictable and occur at inconvenient times. Planned maintenance can help minimize disruptions.
