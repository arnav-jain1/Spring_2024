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
	This will search for both