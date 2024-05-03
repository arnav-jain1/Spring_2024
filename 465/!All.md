# Lec 2
# Intro

* NIC: Network interface card
  * Allows wifi
* RJ45: Ethernet connections

# MAC Address

* Each NIC Has a unique MAC (Media access control) Address: Unique identifier for communication
  * For hardware level
  * 00:A0:C9:00:11:22
  * The first 3 (00:A0:C9 is the manufacturer) and the second 3 is the ID
* Different for each port unless the port in bonded to behave like one port

# IP Address
* IP address (Internet protocol): Numerical label for each device in a computer network that uses Internet protocol for communication
  * Binary address stored in text files displayed in human readable format
  * IPv4: 32 bits
    * 4 bytes, represent with 4 numbers separated by periods
    * 2 parts: Network number and host number
      * Class A: 1.\*.\*.\* to 126.\*.\*.\* (first number is network number) 
	      * 16m hosts on each of 127 networks
      * Class B: 128.1.\*.\* to 191.255.\*.\* (First two numbers are network numbers)
	      * 65k hosts on 16k networks
      * Class C: 192.0.1.\* to 223.255.254.\* (First three are network numbers)
	      * 254 hosts on each of the 2 million networks
      * Private network has its own range. not routable and used internally
  * IPv6: 128 bits
    * 6 bytes, use first 4 sets of 4 hex numbers
    * 1234:5678:9abcd:e012::
	    * The rest are 0s which are usually omitted
    * Two functions: 
      * Google coz too fast

* IP address for software, MAC address for hardware
  * IP address changes while MAC does not
  * Navigation analogy
    * MAC address only focuses on the next turn, the IP address focuses on every turn and is changing
* If you do ifconfig it is the inet

## Virtual Ports
* Allow applications to share hardware resources without interfering with each other (16 bit number \[0,65535])
* 3 ranges
  * Well-known ports: \[0,1023]
    * 20, 21: File transfer protocol
    * 22: Secure shell
    * 80: HTTP
    * etc.
  * Registered ports: \[1024,49151]
    * 25565: Minecraft
  * dynamic/private port: \[49152,65535]

## Linux
* Use ifconfig to get IP address
* lo is the loopback address to test stuff

# Lec 3
# OS and Kernel

* Kernel is between hardware and user
* The shell is the interface between kernel and user

## Root and system

* Root and system are the highest privileged users and provide complete control of the OS
* su: superuser- become root
* sudo: superuser do- Ask root to do something

## Local vs Remote shells
* Local shells are how to look into the local machine's programs, files, etc.
  * Terminal/Command Prompt
* Remote shells are a view into remote system's programs, files, etc.
  * SSH


## Server
* A server is a system with special computational power, resources, etc. that provides access to itself to clients
	* HPC
* They are available to the word and have open ports

## Commands
- Usually multiple ways to do the same thing
- Have flags to specify what to do
- A command's executable binary code is stored within the computer for later use. Usually /usr/bin/*command*
## Tools
* NMap: Discovers open ports on a network, devices connected + more
* Metasploit: 
  * Need to specify RHOST which is who to attack
  * Can send programs to a specific target to mess with it# Lec 4
# Command Line basics
Help flags exist to provide documentation
Control + Z: Suspends a process and places it in the background 
	It is still alive but doesn't actively use the terminal session 
Control + C: Kills the program (also kill)

top: Shows memory, cpu usage and currently running programs. 
htop: top but cooler 
ps: See currently running processes and IDs
ifconfig: Show network info
ping: Check connectivity with a website
curl/wget: Get files over a network 
ssh/scp: Secure shell and secure copy

\> store output to the file
< Input to 
| pipe

## Installing packages
Done through package managers so that dependencies, updates, removal, etc. are done in a consistent way


## LAMP
Open source Web Dev platform allowing users to write apps
Software stack that includes
	Linux
		Open source OS with many distros
	Apache (web server)
		Free web server to host websites
		Parses php and delivers to browser
	MySQL
		DBMS for storage
	PHP 
		Scripting language to create dynamic websites
		Done on the server side and user can't see the php code
		info.php is the first php created
Can substitute so like you can use Python instead of php or PostgreSQL 

# Lec 6
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

# Vulnerability scanning
After scanning the network, attackers can look for vulnerabilities manually or automatically
	Usually are automated tools that scan hosts and networks for known vulnerabilities and weaknesses
	Used together with other recon info to prepare for attacks
<mark style="background: #FF5582A6;">Highly Illegal to do it on the web because it is like getting a blueprint of someone else's house. Need to own both host and infrastructure to do safely</mark>
![[Pasted image 20240320192930.png]]
Vulnerability Assessment Tools (VAS): 
	Nessus
		Proprietary (used to be open-source)
		Free for home use
		Run on windows, linux, etc.
    OpenVAS
		Open Source Nessus fork
		runs only on linux

## Nessus
Two major components
    Server
        Database for vulnerabilities
        Scanning engine
    Client
        Run scans and see results of a scan

Plugins: Simple program that checks for a flaw
    Every audit is coded as a plugin
    Can write new plugins using Nessus Attack Scripting Language (NASL)
	Over 200k for NESSUS and over 130k for OpenVAS (kinda misleading though)
	Many families like firewalls, backdoors, brute force, etc.

Results
	Many severity ratings critical -> high -> medium -> low -> info
	Needs to be interpreted by the user
	Used to search for or create exploits

Internet (Interconnected network)
	Every device has incoming and outgoing ports
	This will search for both# Lec 7
# SQL
Domain specific language used to communicate with relational dbs
	Manage stored data 

## SQL Injection
Root cause: Input being interpreted as a SQL command
Usually done by "Injecting" sql query into a web form
Two main types:
	Blind: DB does not give user info after submitting the query
	Non-Blind: User gets info from query

Easiest way (if possible) Use 1 = 1. This is always true so it will give as much info as you can specify

# Lec 9
#  Overview

## Exploits
Pieces of software, chunks of data, or sequences of commands that take advantage of a bug/glitch/vulnerability to get *unintended* behavior to occur (like getting control of the system, allowing root access)

Remote Exploits: Work over a network and do not require prior access to the system 
Local Exploits: Requires prior access to the system and usually increases the privileges of the attacker (ex: Cycle servers)  



There are resources that contain information and code for exploiting different vulnerabilities such as https://www.exploit-db.com/

## Examples
In Ubuntu 11 and below, you can buffer overflow the ftp client and get higher privileges without the password
In Apache 1.3.x, 2.0.x through 2.0.64, and 2.2.x through 2.2.19 attackers can increase CPU utilization a lot to deny actual users access
# Metasploit
Was a portable network tool in perl in 2003
Turned into a pen testing framework in Ruby around 2007
Modular approach: Any payload with any exploit
Been deemed as dangerous but it is an industry standard 
Adopted by Rapid7 
	Gave it a GUI, scanning capabilities, and automatic exploit execution (Metasploit Pro) 

4 Main modules
	Exploits: Actual exploit to target vulnerabilities 
	Payloads: Code to run remotely
	Auxiliary: Includes port scanners, fuzzers, and customization tools
	Encoders: Convert one format to another

All of these 4 together allow metasploit to exploit vulnerabilities # Lec 11
# Passwords
Bad password:
	Easy to guess or hard to remember
Good password: 
	Hard to guess and easy to remember
Weak passwords can be guessed or cracked
Obviously tradeoffs exist

## Hashing
Function that takes any length of text and results in a "unique" string with a fixed length
A (even slightly) different input must result in a completely different output
It must be impossible to reverse the hash to get the original string
The uniqueness aspect is essentially guaranteed because of how many possible outputs there are 
## Authentication database
Stores users' credentials in a hashed format
## Guessing
Automated trial of default, well-known passwords
Advantage: No special access to the target system
Disadvantage: Likely to be detected or logged

## Cracking
Need a copy of the authentication database that is hashed
Run a tool (below) that can crack the hash and recover the passwords
Offline but requires the database which is hard
### THC-Hydra and Medusa
Fast network logon crackers which support many services
Guess passwords on many network services (FTP, HTTP, VNC)
Similar but work in different ways

Forked Process: The parent processing thread creates a new process that has a copy of a part of the parent process to do the task so that if something happens to the child process the parent is still thriving
	Costs a lot more
	Bit safer in case anything goes wrong
	Hydra
Process threads: Similar but threads share state and memory space
	Faster but more unsafe and complex
	Medusa

## Cryptographic Hash
Input is a variable length message, output is a unique fixed-length string
One way, output does not give input and input always has same output

## Brute force cracking
Try all possible combinations of length 1, 2, etc. Hash them and see if it is the same as the hash you are trying to crack. 
Problem is this takes forever
	$62^{8}$ possibilities if 62 possible characters and 8 characters long
GPU can speed this up but will still take a loooooong time

## Dictionary attacks
Password dictionaries are lists of commonly used passwords
	Available online and can be checked in a few hours
If the password is in the dictionary it WILL be cracked, if not it WILL NOT 

## Hybrid attacks
Many people use the words from the dictionaries but varied slightly (capitalization, number substitutions)
Hybrid Cracking applies common transformations to guess passwords
	Ex: password --> Password PASSword p4ssword P4\$$w0rd
John the Ripper can do Hybrid, brute force, dictionary (from input)

## Rainbow tables
Pre-computed lookup tables for getting passwords from hashes
Trading CPU space at the cost of a LOT of storage
Easiest way to think of it is like a bunch of hashes with their ID as well as associated password
In actuality it is like this for storage purposes
![[Pasted image 20240320204632.png]]
One tool is OPhcrack 

# LM Hashes
Used by old windows versions to store the login password
How it works:
	Must be <= 14 chars
	String is padded to 14, if under
	lower case is converted to uppercase and then split into half
	Each half is encrypted then concatenated to form the final hash

Newer windows uses MD4 (kinda unsecure)
Linux salts the value then hashes result


# Salting
Add a value start or end of the input so that it is even harder to crack# Lec 13
# Cryptography

Mathematical way of protecting sensitive info
4 main primitives
	1. Hashing
	2. Symmetric encryption
	3. Asymmetric encryption
	4. Digital Signature
# Hashing
H(m) = c
Function that turns an input of any length into a fixed-length output
	Must be easy to compute
	One way, <mark style="background: #FF5582A6;">can't derive input from output</mark>
	Unique, can't get same output from different inputs
	If input is different, output is different
SHA256, MD5

## Salting
Used in coordination with hash
Concat to input string in order to increase input space and difficulty of brute force attacks


# Symmetric Encryption
Encryption and decryption from same key
Kerckhoff's principle: Cryptosystem should be secure even if everything except the key is known
## Problem
Each pair of communicating parties needs a shared key
Leads to O(n^2) keys for n parties 
Also needs a key-management system or agreement because how do two entities agree on a key?


# Asymmetric Encryption
Every party has a public and private key that are mathematically linked but cannot be inferred from the other
Encoding is done from the public key and decoding is done from the private key
The only secret is the private key
Does not need O(n^2) keys or a secure channel to transmit the public key 
Slower than symmetric

Use:
	Using my public key a message is encrypted then sent.
	Once I receive it ONLY I can decrypt it with my private key

# Digital Signature
Based on asymmetric encryption

Before the signature is applied, a message is hashed that is unique
The hash is then encrypted using a private key which is the signature. This signature is added on to a message
The recipient then decrypts the hash using the senders public key and then verifies that the hash revealed is the hash that is expected, thus confirming the sender's identity and message authenticity 
This ensures that the message was not tampered with


# <mark style="background: #ADCCFFA6;">Message Authentication Code (MAC)</mark>
Based on symmetric cryptography 
hash with a shared key
Only holder of the shared key can generate a valid MAC tag
Its like Digital signature but symmetric encryption so only one person can verify instead of the whole world# Lec 14
# <mark style="background: #ADCCFFA6;">SSH</mark>
SSH uses asymmetric encryption in order to protect info from people 
Secure channel
	Messages encrypted using shared secret key
	Then authenticated 
	Uses public-key to authenticate the user at the end of the channel
Challenge response protocol
	Server has zero knowledge 
	Hash function isolates the private key

## SSH Agent
Essentially, a way to connect to the SSH server through a good man in the middle where the agent does the same actions as the initial user and the user doesn't need to keep typing in the password on each time because the private key is stored in memory

Private key must be protected by a passphrase 
The passphrase is used to generate a key that encrypts the private key on the local file system
SSH Agent can load the private key into memory and perform the challenge resposne protocal for the user
	User just has to enter passphrase when the agent retrieves the key
![[Pasted image 20240320213340.png]]
Commucation between the ssh client and the agent must have file protection so you can't connect to someone else's client.

## Agent forwarding
![[Pasted image 20240320213558.png]]
Alice can contact SSH Agent that bob is using through SSH if Bob allows
	Alice becomes the man in the middle
	Useful when Bob wants to login to other machines from ALice
	Root user can always connect to forwarded agents
	Private key can never leave the user though

# Terminal
Types:
	Local: Direct access
	Remote: remote access through ssh# Lec 15
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
	 # Lec 16
![[Pasted image 20240320220108.png]]
Packets have headers and information

# Scapy
Written in Python to send, sniff, dissect, and forge packets
	Interactive mode
Allows you to create tools to do a lot
Replicates functionality of nmap, others
Craft a packet with: 
```py
a=IP(dst="172.16.0.1")/TCP(dport=80)/"This is my message"
```
and then send it with send(a)
can also see a human readable format with a.show()
Lots of other stuff as well# Lec 17
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

## Sloworis 
Keep as many connections to the target server open as long as possible

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
# Lec 19
# Intrusion detection system (Snort)
Software to detect malware
Types:
	Network
	Network Node
	Host
	Protocol-based (Http)
	Application-based
Methods:
	Signature based
	Anomaly based
	Hybrid

## SNORT
Industry standard IDS
![[Pasted image 20240328172615.png]]
Essentially an antivirus
Rules:
![[Pasted image 20240502161757.png]]# Lec 22
# WEP
SSID: Service set identifier (network name)
BSSID: Basic SSID (unique identifier for network)

802.11 a/b/g/n/ac/ax (ax is wifi 6)
2.4 GHz is slower but covers further while 5 GHz is faster but shorter distances

## Wireless channels
Frequency bands divided into smaller bands called channels with some overlap
![[Pasted image 20240430174022.png]]

# Wireless Security Protocol
Set of rules and conventions for communication between devices

Wardriving/Warwalking/Warbiking: Search for wifi networks while in a motor vehicle, walking, biking, etc. using a portable device
Allows people to sniff networks

## Wired Equivalent Privacy (WEP)
Security algorithm for wireless networks that's old and outdated
Uses RC4 Stream cipher for encrypting and CRC-32 Checksum for integrity
Many flaws

Pigeonhole principle: If there are more pigeons than pigeonholes, then there must be pigeonholes with multiple pigeons 
Birthday paradox: If there are 23 people in a room, the odds of two having the same birthday are 50%
![[Pasted image 20240430174604.png]]
IV Changes and gets concat with key, having two same IVs we can get the key
<mark style="background: #ADCCFFA6;">Since the IV is only 24 bits, Pigeonhole princple says the IV will eventually start repeating </mark>
<mark style="background: #ADCCFFA6;">Bday paradox helps show that after a surprisingly small number of IVs (5000), there is a high chance that some IVs are going to be reused</mark>
Vernam cipher: Key XOR text = cipher; cipher XOR key = text. 
	Key must be truly random

WEP is also very slow

## WPA and WPA 2
Wifi protected access 
WPA uses TKIP encryption and MIC (stronger than CRC) but TKIP has a flaw (you can reinject the keystream and spoof it)
WPA2 uses CCMP (AES encryption) and MIC (message integrity check)

WEP -> WPA -> WPA2 -> WPA3

### WPA-PSK and WPA2-PSK
For home and small offices, no authentication server
Each device authenticates using 256-bit key made from the password
Vulnerable to offline password cracking if there is a weak password

Vulnerable to Key reinstallation attacks (KRACKS)
	Force unneccesary resets through replay attacks
	forward-secrecy is affected
	Several variants
## WPA-Enterprise and WPA2-Enterprise
For companies, requires RADIUS authentication server
Vulnerable to Key reinstallation attacks 
## WPS
Alternative authentication key to simplify and make the process stronger
Has major security hole
The 8-digit pin has 3 parts: 4 digit, 3 digit, and checksum (integrity check)
meaning 10000 + 1000 = 11000 combinations

### Offline dictionary attack
Stealthy because you only need one packet and then the rest is offline
Challenge: Starting the initial handshake 
Downside: If password is not in dictionary it won't be found
Works on WPA/2 personal

### WPS attack
Pin is hard coded, always the same
Might take a bit to get the pin and it might crash the network
Only works on WPA2 

### KRACKS
Works on all WPA2 but complex and may crash network


# WPA3
Next generation with cutting edge security
Not fully rolled out
Have latest security methods, doesn't use old protocols, requires protected management frames

Protects against dictionary attacks and forward secrecy 
Some security concerns like downgrade attacks, side-channel leaks


# Conclusion
Dont use WEP 
Use strong password for WPA1/2
WPA3 eventually

# Lec 23
# Rootkit
Type of malware in your computer
5 types
1. Kernel mode
	Installed with kernel level permissions
	Loaded as a module in the kernel
		Dynamic, doesn't need full recompliation 
	Like device drivers
	Anything can be done by attacker including installing keyloggers, hiding files, removing logs
2. Application
	Target specific applications 
	Bugs in the app allow a way for attackers to get in and hide folders, modify registries, open ports
	Modifies behavior of apps, tracks usage
1. Memory 
2. Bootloader
3. Hardware

Prevention: Block phishing emails, keep up to date with antivirus, be wary of opening downloaded files
Kernel level rootkits are only 100% mitigated if you reinstall the OS (same with memory rootkits)
	NOT the case with bootloader or firmware

# Lec 24
# Logging and Auditing 
Logging: Process of recording events and stats to get information about a system
	Stores entries for failed logins/logouts, creation of accounts, executing commands, file access, turning on/off system/services
	Mechanism to analyze security state
		Can determine whether a requested action will make the system vulnerable
		Can see the events leading to system being vulnerable
	Common file names and usage (all in /var/log/)
		syslog: General messages and system info
		auth.log: Authentication logs
		kern.log: kernel logs
		mail.log: Mail server logs
		boot.log: System boot log
		also folders such as /var/log/apache2/ for apache logs
Auditing: Process of analyzing recorded logs
	Manual or automatic


## Syslog
Protocol for computer message logging based on UDP
Seperates generating entity (devices) with logging entity (server)

## Manual
Windows: 
	Configed thru Local Security Policy
	Audit events using Event viewer
	Task manager
macOS:
	Can view records using app called Console
Linux: 
	Distribution specific but config through /etc/rsyslog.conf on Ubuntu 
	Or audit by displaying /var/log
	Other auditing commands:
		who: Users currently logged in
		last: last users to log in
		ac: connection times for each user
		ps: Currently displaying processes 
		top: currently running processes (htop)
		netstat: network connections

## Automated Auditing 
Tools that process 
	Application logs (Web/mail/db servers etc)
	System logs
	Security logs

Freeware tools:
	AWStats (linux)
	Log parser 2.2 (Windows)

## Attackers
Alter logs to cover tracks
Can:
	Delete all logs
	Delete suspicious events (failed logins, file modification, error)
	Cover tracks using rootkits
Bare minimum to protect: 
	Proper permissions
	Append only
Better:
	Encrypt logs so only alterable with proper key
Best:
	Seperate log server
	Config so that logs redirected to centralized server
	Host compromised does not allow attacker to alter stored logs
# Lec 25
# Security Onion
Free and open source linux distribution for
	Intrution detection
	Security monitoring 
	Log managment 
	Includes Snort, Logstash, and a lot more

Part of Ubuntu
Security tools pre-installed 
Configuration wizard for install

## Elastic Stack (ELK)

- Elastic Search
	- Distributed
	- Restful
	- non-relational db
- Logstash
	- Pipline for centralizing, transforming, and stashing data
- Kibana
	- Visualize # Lec 26
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

