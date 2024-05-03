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
Lots of other stuff as well