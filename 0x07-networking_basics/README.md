
# Networking basics #0

---

## OSI MODEL

![Alt text](4e6a0ad87a65d7054248.png)
![Alt text](0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg)

The OSI (Open Systems Interconnection) model is a conceptual framework that provides a standard way of describing how different networking protocols and technologies communicate with each other. The model consists of seven layers, each of which is responsible for a specific aspect of network communication.

    Here are the seven layers of the OSI model, listed in order from the lowest to the highest:

    1. Physical layer: This layer is responsible for the physical transmission of data over a network, including the transmission medium, connectors, and electrical signals.

    2. Data link layer: This layer is responsible for controlling the flow of data between network devices, including error detection and correction, and addressing.

    3. Network layer: This layer is responsible for routing data between different networks, including addressing and packet forwarding.

    4. Transport layer: This layer is responsible for reliable end-to-end delivery of data, including error detection and correction, and flow control.

    5. Session layer: This layer is responsible for managing the session between network devices, including establishing and terminating connections, and managing data exchange.

    6. Presentation layer: This layer is responsible for data representation and encryption, including converting data into a format that can be transmitted over a network and compressing data to reduce transmission time.

    7. Application layer: This layer is responsible for providing network services to applications, including email, file transfer, and web browsing.

The OSI model provides a standardized way of understanding how different networking protocols and technologies work together. By breaking network communication down into distinct layers, the model allows for greater flexibility and interoperability between different systems and devices. The OSI model is often used as a reference model for network designers and developers to ensure that their systems adhere to standard networking principles.

---

## LAN

A LAN, or Local Area Network, is a computer network that connects devices within a limited geographic area, such as a home, office building, school, or a small group of buildings in close proximity. The primary purpose of a LAN is to facilitate communication and data sharing among devices within the network.

### Typical usage of a LAN includes:

    File sharing: Users can access and share files stored on shared network drives or devices.
    Printing: Multiple users can share a single network printer.
    Internet access: A LAN often provides internet connectivity to all connected devices through a router.
    Email and messaging: LANs enable communication between users through local email servers or messaging applications.
    Software and resource sharing: Users can access shared software applications and network resources.

### Typical geographical size:

    The geographical size of a LAN is relatively small compared to other types of networks. It can cover an area as small as a single room or as large as a few kilometers.

## WAN

A WAN, or Wide Area Network, is a type of computer network that spans a large geographical area, connecting multiple LANs or other networks over long distances. Unlike LANs, which are confined to a limited geographic area, WANs can cover cities, countries, or even global regions. WANs are designed to facilitate communication and data exchange between different locations

### Typical usage of a WAN includes:

    Interconnecting multiple LANs: WANs are used to link different local networks (LANs) at various locations, allowing seamless communication and resource sharing between them.
    Data transmission between geographically dispersed sites: WANs enable organizations to transfer data, applications, and information between offices or data centers located in different cities or countries.
    Internet connectivity: WANs provide access to the internet for all connected locations, allowing users at different sites to access online resources and services.

## What is the Internet?

The Internet is a global network of interconnected computers and servers that allows users worldwide to access and share information and resources. It is a vast collection of networks that use standardized communication protocols, such as TCP/IP (Transmission Control Protocol/Internet Protocol), to facilitate data exchange.

### IP

An IP address, or Internet Protocol address, is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host or network interface and providing the location of the device in the network. IP addresses are crucial for routing data packets across the Internet, ensuring that information reaches its intended destination. They are represented in either IPv4 (32-bit address) or IPv6 (128-bit address) formats.

#### There are two types of IP addresses:

    IPv4 (Internet Protocol version 4): This is the most common type of IP address used on the Internet. It consists of 32 bits and is expressed in four decimal numbers separated by periods (e.g., 192.168.0.1). However, due to the rapid growth of internet-connected devices, the available IPv4 address space has become limited.

    IPv6 (Internet Protocol version 6): IPv6 was introduced to overcome the limitations of IPv4 and provide a much larger address space. It uses 128 bits, allowing for a practically unlimited number of unique IP addresses. IPv6 addresses are written in eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

### What is localhost?

    "Localhost" refers to the loopback network interface on a computer, usually with the IP address 127.0.0.1 in IPv4 or ::1 in IPv6. When a program or service running on the same machine tries to access the network using "localhost" as the destination, it redirects the connection back to itself. In other words, it acts as a way to access services on the local machine without going through an external network. This is often used for testing and development purposes.

### What is a subnet?

A subnet, short for subnetwork, is a portion of a larger network that is logically separated from the main network. It allows network administrators to divide a large IP address space into smaller, more manageable segments. Subnets help in controlling network traffic, reducing network congestion, and improving security by isolating different parts of the network from each other. Devices within the same subnet can communicate directly with each other without going through a router, while communication between devices in different subnets requires routing.

## Main difference between TCP and UDP:

    Reliability: TCP is a reliable, connection-oriented protocol. It ensures that data packets are delivered in the correct order and without errors. If any packet is lost or corrupted during transmission, TCP automatically retransmits it, guaranteeing the delivery of data. On the other hand, UDP is an unreliable, connectionless protocol. It does not guarantee data delivery or order and does not perform retransmission. It is often used for time-sensitive applications where some packet loss is acceptable, such as real-time video streaming or VoIP.

    Connection Establishment: TCP requires a three-way handshake process to establish a connection between the sender and receiver before data transfer. UDP does not have a connection setup phase; it simply sends packets to the destination without establishing a connection.

    Overhead: TCP has more overhead due to its reliability mechanisms, including acknowledgment packets, sequence numbers, and flow control. UDP has less overhead since it does not include these additional mechanisms.

    Order of Delivery: TCP guarantees the order of delivery of packets, so they are received in the same order they were sent. UDP does not guarantee the order, and packets may arrive out of order.

## What is a port?

A port is a numeric identifier used to distinguish different services or processes running on a device within a network. It helps the operating system identify which application or service should handle incoming data packets. Ports are essential for enabling communication between various services and applications over a network.

### What are SSH, HTTP, and HTTPS port numbers?

    SSH (Secure Shell) uses port number 22.
    HTTP (Hypertext Transfer Protocol) uses port number 80.
    HTTPS (Hypertext Transfer Protocol Secure) uses port number 443.

SSH is a secure protocol used for remote access to devices and servers. HTTP is the standard protocol for transmitting web pages and other content over the internet. HTTPS is the secure version of HTTP, where the communication is encrypted using SSL/TLS protocols to ensure data privacy and integrity.

## What tool/protocol is often used to check if a device is connected to a network?

The tool/protocol often used to check if a device is connected to a network is "Ping." Ping is a network utility used to send a small packet of data to a target IP address or hostname and waits for a response. If the target device is reachable and connected to the network, it sends back a response (usually an acknowledgment). The response time, known as round-trip time, is measured and displayed, providing information about the network latency and connectivity status. Ping is widely used for network troubleshooting and monitoring.

## netstat command (network statistics)

Command line tool that is used to
display the current network
connections and port activity on
your computer.

The `netstat` (network statistics) command is a network utility available in various operating systems, including Windows, Linux, and macOS. It allows users to view detailed information about network connections, routing tables, network interfaces, and other related statistics. The command can be run from the command-line interface (CLI) or terminal.

In its basic form, the `netstat` command displays a list of active network connections on the system. The output typically includes the following information:

1. Protocol: The communication protocol used for the connection, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).

2. Local Address: The IP address and port number of the local endpoint of the connection.

3. Foreign Address: The IP address and port number of the remote endpoint with which the local system is connected.

4. State (for TCP connections): The current state of the TCP connection, indicating if it is established, listening, closed, etc.

Here is an example of the output of `netstat`:

```
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 192.168.1.10:48294      151.101.129.69:80       ESTABLISHED
tcp        0      0 192.168.1.10:43774      74.125.24.113:443       ESTABLISHED
udp        0      0 0.0.0.0:5353            0.0.0.0:*
```

Some common options and their meanings for the `netstat` command:

- `-a` or `--all`: Display all connections, including listening and non-listening sockets.
- `-t` or `--tcp`: Show TCP connections.
- `-u` or `--udp`: Show UDP connections.
- `-n` or `--numeric`: Display IP addresses and port numbers in numeric form (avoids hostname resolution).
- `-p` or `--program`: Show the process ID (PID) and program name associated with each connection.
- `-r` or `--route`: Display the routing table.
- `-s` or `--statistics`: Show network statistics.

Note that the specific options and their behavior may vary slightly depending on the operating system being used. Additionally, some versions of `netstat` may be deprecated in favor of other tools, such as `ss` (Socket Statistics) on newer Linux distributions. Therefore, it's always a good idea to consult the command's documentation or the relevant man pages for more detailed usage information on your specific system.
**man netstat**

## ping/ICMP

Ping is a network utility used to test the reachability and responsiveness of a host or network device on an Internet Protocol (IP) network. It is available in most operating systems and is commonly used for network troubleshooting and diagnostics. The term "ping" comes from the sonar concept, where a sound pulse is sent and echoed back to determine the distance to an object.

Ping operates by sending Internet Control Message Protocol (ICMP) Echo Request messages to the target host and waiting for ICMP Echo Reply messages in response. ICMP is a network layer protocol that is part of the IP suite, and it is used for various network-related tasks, including reporting errors, diagnostics, and signaling.
**man ping**

