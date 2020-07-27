import ast 
import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  



class AESCipher(object):

    def __init__(self, key):
        self.key = pad(bytes(key, 'utf-8'), 16)

    def encrypt(self, message):
        res = isinstance(message, dict)
        if res:
            json_data = { "key": "value"}
            message = json.dumps(json_data)

        message = bytes(message, 'utf-8')
        raw = pad(message,16)
        cipher = AES.new(self.key, AES.MODE_ECB)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        dec = cipher.decrypt(enc)
        res1 = unpad(dec,16).decode('utf-8')
        try:
            res2 = ast.literal_eval(res1)
            print(type(res2))
            return res2 
        except:
            print(type(res1))
            return res1

key = "your_key"

# ---------> str
message = 'rahul'

# ---------> json/dict
# message = { "key": "value"}
# message = json.dumps(message)

encryption = AESCipher(key)

encrypt_msg = encryption.encrypt(message)
decrypt_msg = encryption.decrypt(encrypt_msg)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypt_msg}")
print(f"Decrypted Message: {decrypt_msg}")
