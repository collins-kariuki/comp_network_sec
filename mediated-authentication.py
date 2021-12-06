# Kuria Collins Kariuki
# P15/130005/2018
import uuid
from symetric_key import encrypt, decrypt
from datetime import timedelta
# Key Distribution Network KDC


class KDC:
    ''' 
        Key Distribution Centre contains the Authentication Server, User DB and the Ticket Granting Server 

    '''

    def __init__(self, name):
        self.name = name
        self.AS_TGS_key = input("Enter Ticket Gen Server key")
        self.TGS_file_server_key = input("Ebter db_key")
        self.user_AS_key = input("Ebter user_key")
        self.db = {
            '1qase34rfgy7yujm': 'kuria'
        }

    def auth_server(self, cipher):

        user_pass_hash = decrypt(cipher, self.user_AS_key)

        if self.db.get(user_pass_hash):
            return encrypt(user_pass_hash, self.AS_TGS_key)
        else:
            return "Auth failed"

    def TGS(self, TGT):
        user_pass_hash = decrypt(TGT, self.AS_TGS_key)
        if self.db.get(user_pass_hash):
            token = str(uuid.uuid4) + str(timedelta(hours=4))
            return encrypt(token, self.TGS_file_server_key)
        else:
            return "Auth failed 2"

    def file_server(self, ticket):
        token = decrypt(ticket, self.TGS_file_server_key)
        return print(token)


key_centre = KDC("kdc1")

pass_hash = "1qase34rfgy7yujm"

pass_cipher = encrypt(pass_hash, key_centre.user_AS_key)

TGT = key_centre.auth_server(pass_cipher)

ticket = key_centre.TGS(TGT)

token = key_centre.file_server(ticket)
