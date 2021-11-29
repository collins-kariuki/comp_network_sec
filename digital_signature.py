# Kuria Collins Kariuki
# P15/130005/2018
import math
import hashlib

# generate prime numbers
from Crypto.Util import number
primes = [number.getPrime(8), number.getPrime(8)]

print("\nPrime numbers are: " + str(primes))


# n - first part of public key
n = primes[0]*primes[1]

# phi of n
phi_of_n = (primes[0]-1) * (primes[1]-1)

# generate co-prime (e) of Phi of n 1 < e <phi of n
e = 5

# for n in range(phi_of_n):
#     if math.gcd(n, phi_of_n) == 1:
#         e = n
print(e)
privatekey = [n, e]
print("\nPrivate key is " + str(privatekey))

# generate d e.d = 1 mod phi of n
d = (1 % phi_of_n) / e

publickey = [n, d]
print("\nPublic key is " + str(publickey))

# user Input
message = input("\nPlease enter message: ")

print("Message to be sent: " + message)
sent_plain_text = message

# md5 hash
hashed_message = hashlib.md5(message.encode("utf-8")).hexdigest()
print(hashed_message)

# Encryption:
ciphertext = []
for char in hashed_message:
    conv_plain = ord(char)
    ciphertext.append(pow(conv_plain, publickey[1]) % n)

print(" \n Cipher text is: \n" + str(ciphertext) + "\n")

# Decryption:
decrypted = []
for ciph in ciphertext:
    decypted_ciph = round(pow(ciph, privatekey[1]) % n)
    decrypted.append(chr(decypted_ciph))
    message = "".join(decrypted)


print("Decrypted Cipher :  " + message)

# Compare hashes
print("Message Received: " + sent_plain_text)
myhash = hashlib.md5(sent_plain_text.encode("utf-8")).hexdigest()
print("My hash :  " + myhash)

if myhash == message:
    print("The message is valid")
else:
    print("Message is corrupt")
