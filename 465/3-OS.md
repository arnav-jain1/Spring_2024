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
  * Can send programs to a specific target to mess with it