# Kuria Collins Kariuki
# P15/130005/2018
import uuid
from symetric_key import encrypt, decrypt
# Key Distribution Network KDC


class KDC:
    ''' Key Distribution Network contains the Authentication Server, User DB and the ticket granting service '''

    TGS_key = "11234rtghjko0987ytf"

    def __init__(self, name):
        self.name = name
        self.TGS_key = input("Enter Ticket Gen Server key")
        self.db_key = input("Ebter db_key")
        self.user_key = input("Ebter user_key")
        self.db = users = {
            '1qase34rfgy7yujm': 'kuria'
        }

    def auth_server(self, cipher):
        self.user_key
        self.db_key

        user_recv = decrypt(cipher, self.user_key)

        db_AS_cipher = encrypt(user_recv, self.db_key)

        user_id = decrypt(db_AS_cipher, self.db_key)

        if self.db.get(user_id):
            token = str(uuid.uuid4)
            return encrypt(token, self.TGS_key)

    def TGS(self, TGT):
        TGT = decrypt(TGT, self.TGS_key)
        return encrypt(TGT, self.user_key)

    def file_server(self, ticket):
        token = decrypt(ticket, self.user_key)
