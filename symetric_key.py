# Kuria Collins Kariuki
# P15/130005/2018

print("\n...Symetric Key encryption...\n")

message = input("Please enter your message: ")
key = input("Enter the key: ")


def encrypt(message, key):
    cipher = []
    key_index = 0

    def encr_func(message_index, key_index):
        cipher.append(ord(message[message_index]) * ord(key[key_index]))

    for message_index in range(len(message)):
        if (message_index > 0) and (message_index % 8 == 0):
            if key_index == len(key):
                key_index = 0
                encr_func(message_index, key_index)
            else:
                key_index = key_index + 1
                encr_func(message_index, key_index)
        else:
            encr_func(message_index, key_index)

    return cipher


def decrypt(cipher, key):
    key_index = 0

    def decry_func(cipher_index, key_index):
        message = []
        message.append(
            chr(cipher[cipher_index] // ord(key[key_index])))

    # split_cipher = cipher.split(", ")
    # print(split_cipher)
    for cipher_index in range(len(cipher)):
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


cipher = encrypt(message, key)
print(cipher)

decrypted_message = decrypt(cipher, key)
print(decrypted_message)
