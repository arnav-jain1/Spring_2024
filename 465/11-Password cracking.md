also lec 10
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
Process threads: Similar but threads share state and memory space
	Faster but more unsafe and complex

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
Add a value start or end of the input so that it is even harder to crack