The RSA algorithm is an asymetric cryptography technique used in secure data transmission. This is done through a system of private and public keys used to encrypt and decrypt data.
Using the distribution of prime numbers and the limitation of modern computing, RSA cryptography prevents the algorithm from being decrypted without the proper keys. 
In this Cryptography respository, you will find the code to generate public and private keys, the code to encrypt data using the public key, and finally the code to decrypt the data with the private key

To properly use this program, you will need to get familiar with these three scripts:

1. Generate keys: This program creates a set of public key and private keys through a series of functions below

Public Key = (e, N)

* N = pq; p & q are random prime numbers

* e = {1<e<phi(N); coprime with N & phi(N)

* where phi(N) = (p-1)(q-1)

Public Key = (d, N)

* de = (mod phi(N)) = 1


2. Encryption: Using the Public Key, you are able to encrypt a given message

The message is first converted into a 256-byte code then into a singular integer; from that integer, the message is encrypted with the RSA algorithm:

* C = (M^e) mod N


3. Decryption: Using the Private Key, you are able to decrypt a given encryption

The message that underwent cryptography is first decrypted using the formula:

* M = (C^d) mod N

then is converted back into 256-byte code, and finally converted back into the original data
