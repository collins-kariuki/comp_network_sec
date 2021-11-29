# Kuria Collins Kariuki
# P15/130005/2018

print("\n...Symetric Key decryption...\n")

cipher = input("Please enter the cipher: ")
key = input("Enter the key: ")

message = []


def decrypt(cipher, key):
    key_index = 0

    def decry_func(cipher_index, key_index):

        message.append(
            chr(int(split_cipher[cipher_index]) // ord(key[key_index])))

    split_cipher = cipher.split(", ")
    print(split_cipher)
    for cipher_index in range(len(split_cipher)):
        if (cipher_index > 0) and (cipher_index % 8 == 0):
            if key_index == len(key):
                key_index = 0
                decry_func(cipher_index, key_index)
            else:
                key_index = key_index + 1
                decry_func(cipher_index, key_index)
        else:
            decry_func(cipher_index, key_index)

    return "".join(message)


decrypted_message = decrypt(cipher, key)
print(decrypted_message)
