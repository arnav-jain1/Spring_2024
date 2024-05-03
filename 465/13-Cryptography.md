# Lec 13
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
Its like Digital signature but symmetric encryption so only one person can verify instead of the whole world