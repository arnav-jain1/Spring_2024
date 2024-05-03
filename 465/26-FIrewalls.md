# Lec 26
Like perimeter control 

Used in two places
	Host-based
	Network based
Two functionalities
	Packet filters
	Gateways
![[Pasted image 20240430204303.png]]
Filter rule:
<protocol, srcIP, srcPort, dstIP, dstPort, action>
ORDER MATTERS

Drop or allow packets
	Should drop if no match

Ingress: Input filtering
Egress: output filtering

# Dynamic Packet filtering
Letting in return packets (from outbound messages) is tricky
2 options
	Dynamically insert a new filtering rule to let in return traffic
	Firewall is a transparent proxy between communication parties
![[Pasted image 20240430204605.png]]
Outside communicates to firewall, firewall sends to inside

![[Pasted image 20240430204616.png]]


![[Pasted image 20240430204720.png]]
Network sends to firewall, firewall changes incoming address and sends to user

# FTP problem
Two channels, control and data (port 21 is control)
Active mode: Client issues PORT command to tell the server which port number to connect back
Passive mode: Client has PASV command and server responds with a port number for the client to connect to

Has to use dynamic filtering which is a security risk

# Summary
Current solutions are like bandaids
Defense needs to be automated from a number of devices to be accurate

