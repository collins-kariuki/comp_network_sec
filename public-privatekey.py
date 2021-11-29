# Kuria Collins Kariuki
# P15/130005/2018
import math

# generate prime numbers
from Crypto.Util import number
primes = [number.getPrime(16), number.getPrime(16)]

print("\nPrime numbers are: " + str(primes))


# n - first part of public key
n = primes[0]*primes[1]

# phi of n
phi_of_n = (primes[0]-1) * (primes[1]-1)

# generate co-prime (e) of Phi of n 1 < e <phi of n
e = 5

privatekey = [n, e]
print("\nPrivate key is " + str(privatekey))

# generate d e.d = 1 mod phi of n
d = (1 % phi_of_n) / e

publickey = [n, d]
print("\nPublic key is " + str(publickey))

# user Input
plaintext = input("\nPlease enter message: ")

# Encryption:
ciphertext = []
for char in plaintext:
    conv_plain = ord(char)
    ciphertext.append(math.fmod(pow(conv_plain, publickey[1]), n))

print(" \n Cipher text is: \n" + str(ciphertext) + "\n")

# Decryption:
decrypted = []
for ciph in ciphertext:
    decypted_ciph = round(math.fmod(pow(ciph, privatekey[1]), n))
    print(decypted_ciph)
    decrypted.append(chr(decypted_ciph))
    message = "".join(decrypted)


print("Decrypted message :  " + message)
