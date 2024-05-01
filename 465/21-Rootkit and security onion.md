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
	- Visualize 