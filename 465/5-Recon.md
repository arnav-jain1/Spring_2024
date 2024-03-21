# Reconnaissance
Information gathering to learn as much as possible about target system

2 steps 
Step 1:
	Open source intelligence gathering
		Social Engineering
		Physical Break-ins
		Dumpster Diving
Step 2:
	Scanning
		Use of scanning tools to automatically scan Services, vulnerabilities, hosts. etc.

## The Harvester:
Tool for getting email, name, and other stuff
The legality depends on how it is used. (don't spam it and send too many requests). Otherwise you should be good
Flags:
	-d is domain to search
	-b is the source (search engine) 
	-l is the limit of result
## Nmap
Portscanner, ping sweep, and OS fingerprinting tool
Nmap sends packets in different ways to try and find open ports
Kind of like throwing stones at a house to map out a shape of it
Ping sweep
	Example: <mark style="background: #BBFABBA6;">nmap -sP targetIP</mark>
TCP connect
	Three-way handshake 
	Example: <mark style="background: #BBFABBA6;">	nmap \[-sT] targetIP</mark> or <mark style="background: #BBFABBA6;">nmap \[-sS] target IP</mark>
	Send a packet, recieve a packet, send another packet to establish connection
		Sends SYN
		Await SYN Ack
		Send nothing or RST
	Unlikely to cause problems but easy to detect
UDP
	Send a UDP packet but does not receive a response
	Example: <mark style="background: #BBFABBA6;">	nmap -sU targetIP </mark>
	Useful when a lot of data is being sent
	If the packet is returned then the port is closed
	If no packet is returned then the port is open
	Easy to detect but unreliable 
Xmas Tree scan Mode
	Send TCP segment to a target port with FIN, URG, and PSH code bits set (violation of TCP specification)
	If RST is returned then closed otherwise open
	Example: <mark style="background: #BBFABBA6;">	-sX</mark>
	More stealthy
Null mode
	Sent TCP to target with no code bits set (violation of specification)
	If RST returned then closed otherwise maybe opened
	Example: <mark style="background: #BBFABBA6;">	-sN</mark>
	More stealthy
TCP ACK
	Send a TCP ACK to a target port (violation)
	If RST returned, then packet went through the filter otherwise the packet got filtered
	Example: <mark style="background: #BBFABBA6;">nmap [-sA] target_ip</mark> 
	Used to determine what filters are enabled
Other options
	-p: Set port ranges
	Set source ports so it doesn't get blocked
	Use decoys 

# LEGALITY OF NMAP
Need to own both host and infrastructure to perform a scan safely


