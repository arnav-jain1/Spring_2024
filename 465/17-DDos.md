# DoS/DDoS
DoS stands for denial of service
Attempt by attackers to prevent users from accessing the site or service
multiple attackers/bots coordinating against a target is a DDoS (distributed DoS)

## DoS
Examples:
	Flooding a network so the server can't handle everything
	Disrupting connection between two machines
	Preventing a specific person from accessing a service
	Disrupting a service to a specific system
Classes:
	Vulnerability: Ping of death, nuke
	Reflector: Smurf attack, amplification attack
	Flooding: SYN flood, UDP flood
	Slowloris 

### Smurf attack
Attacker sends Internet Control Message Protocol (ICMP) echo requests, essentially a ping, to an intermediary which then sends pings to multiple devices in the network. The source addresses are generally spoofed
**SOLUTION**: Machines no longer respond to the ICMP echo requests

### Ping of death
Attacker creates a ping with 65510 data octets and sends to the victim. The total size of the packet (65538) is larger than what IP protocol can handle (65536) so devices crashed, froze, or rebooted
**SOLUTION**: fixed by software patches

Nuke attack: Very similar, send a packet that target can't handle thus crashing it.

### DNS amplification attack
Type of smurf attack
1. Target open recursive DNS servers (spoofs source IPs)
2. These servers then spam requests to the victim 
![[Pasted image 20240322170006.png]]
Solution varies 

Memchached amplification:
	Same idea as the DNS amplification
	Target publically routable memcached servers (which then spoofs the IP)
	These servers then send requests to the victim 
	For 1 byte sent by the attacker, 51KB were sent to victim 

### SYN Flood (sloworis attack)
Attacker sends a bunch of TCP/SYN packets (with forged sender address)
Victim machine handles it like a connection request (remember the 3 way handshake)
Victim machine then waits for the final ACK packet but it never comes
There is now a ton of half opened connections so the server can't start any more
Victim cannot respond to legit requests
**SOLUTION**: SYN cookies
![[Pasted image 20240322170605.png]]

### UDP Flood
TONS of UDP packets sent to target
Results: Target host becomes overloaded and can't reply to legit requests
**SOLUTIONS**: not many, like trying to stop a flood as a singular house
	Most UDP filters aren't very good
	ISP needs to help filter

## Tools
LOIC (Low Orbit Ion Cannon)- open source network stress testing application
	3 Types of attacks: UDP, TCP, HTTP
	All open a connection to the target and spam a predefined string (payload)
	String sent in plain text for UDP/TCP or in contents of GET request for HTTP
	Payload is same for every packet
	IP is not spoofed
Trin00
Tribe flood network



# Botnets
Compromised machines controlled by a bad actor 
Mechanisms of control:
	Centralized: Command and control server
		Every computer listens to a central server with a shifting dns
	decentralized: peer to peer
		Each device communicates to a different device giving each other info/data
## Mirai
200k-300k bots
Targets IoT devices using default login info
Used to DDoS
Code is now open source

## Nugache
Trojan that compromises host machine 
Computes list of peers 
Has a P2P mechanism to update, attack

# Detection
Easiest way to detect an attack is to have a network sniffer on the target machine
Block IP addresses sending a ton of packets
