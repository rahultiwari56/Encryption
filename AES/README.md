A Simple Go Encryptor/Decryptor For AES-ECB Mode

The secret key to use in the symmetric cipher. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.

Mode - The chaining mode to use for encryption or decryption (MODE_ECB -Electronic Code Book).

You just have to change the padding of the key if you want to use other than AES-256, For default i have used AES256 as i have used padding 32 for the key

Ex: 
AES-128
self.key = pad(bytes(key, 'utf-8'), 16)

AES-192
self.key = pad(bytes(key, 'utf-8'), 24)

AES-256
self.key = pad(bytes(key, 'utf-8'), 32)