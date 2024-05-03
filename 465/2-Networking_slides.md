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

