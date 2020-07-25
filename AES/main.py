import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  


class AESCipher(object):

    def __init__(self, key):
        self.key = pad(bytes(key, 'utf-8'), 32)

    def encrypt(self, message):
        message = bytes(message, 'utf-8')
        raw = pad(message,16)
        cipher = AES.new(self.key, AES.MODE_ECB)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        dec = cipher.decrypt(enc)
        return unpad(dec,16).decode('utf-8')

key = "your_key"
message = "message_to_be_encrypted"

encryption = AESCipher(key)

encrypt_msg = encryption.encrypt(message)
decrypt_msg = encryption.decrypt(encrypt_msg)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypt_msg}")
print(f"Decrypted Message: {decrypt_msg}")
