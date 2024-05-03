# Lec 15
# Network Sniffing
Process of intercepting and reading network traffic
<mark style="background: #ADCCFFA6;">Data link level of OSI model</mark>

## Network Topologies
Star:
	All connected to one like *
	Our lab
Ring:
	All connected in a circle like O
Mesh:
	All connected to each other like:
	![[Pasted image 20240320214654.png]]
Bus:
	All connected via one line like a BUS
Hybrid:
	A mix

## Wired star Network Environments
Hub environment
	Duplicates data packets received via one port and making them available to all ports
Switched environment
	Sends packets to the correct host without broadcasting to all

### Sniffing wired 
Network card on promiscuous mode
Sniffing a switched environment:
	Sniffs using TAP and SPAN ports
	Placing hub between router and switch
	ARP poisoning 

## Address resolution protocol (ARP)
Used for mapping IP address to MAC address
ARP cache correlates IP to MAC and stores it
Stored on first come first serve basis

### Poisoning/spoofing
Anyone can create ARP requests so attacker sends a fake message claiming they are the gateway
The target will think the attacker is the gateway and send info there (man in the middle)
Defences:
	Using https and encrypted protocol 
	 Monitor applications based on packet filtering
	 Read-only ARP entries
	 