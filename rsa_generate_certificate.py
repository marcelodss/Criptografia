from Crypto.PublicKey import RSA

"""
Fonte: https://devrescue.com/python-rsa-generate-certificate/

O pacote instalado foi Cryptodome mas, ao importar usamos Crypto
"""

new_key = RSA.generate(2048)

private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

print('\nprivate_key:', private_key.decode("utf-8"))
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print('\npublic_key: ', public_key.decode("utf-8"))
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()