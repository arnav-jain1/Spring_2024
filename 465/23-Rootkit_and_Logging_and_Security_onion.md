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
	- Visualize 