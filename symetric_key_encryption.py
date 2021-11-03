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


cipher = encrypt(message, key)
print(cipher)
