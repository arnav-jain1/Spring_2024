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

