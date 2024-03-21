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
	Remote: remote access through ssh