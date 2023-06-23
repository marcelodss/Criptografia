from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

"""
Fonte: https://devrescue.com/python-rsa-encrypt-with-public-key/

Ver: 
- https://betterprogramming.pub/using-linux-rsa-encryption-keys-in-python-d9ab840a81e5
- https://www.thesecuritybuddy.com/cryptography-and-python/how-to-implement-the-rsa-encryption-and-decryption-algorithm-in-python/
- https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html

O pacote instalado foi Cryptodome mas, ao importar usamos Crypto
"""

# ============ GENERATE CERTIFICATE PAIR ============================
new_key = RSA.generate(2048)

private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

# =========== ENCRYPT DATA WITH CERTIFICATE =========================
print("\n")

message = b'CODE EVERYDAY TO GET BETTER'

key = RSA.import_key(open('public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print(ciphertext)

# ========== DECRYPT DATA WITH CERTIFICATE ==========================
print("\n")

key = RSA.import_key(open('private_key.pem').read())
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(ciphertext)
print (plaintext.decode("utf-8"))