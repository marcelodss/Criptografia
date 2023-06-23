from modulos.access_key_fernet import get_key_fernet, get_encryption_as_string, get_decryption_as_string
import datetime

print("=" *80)
# ================================================================================
key_crypto = get_key_fernet("minha chave preferida")
ini = 999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_9
ini = 9

more = 10
for i in range(ini, ini + more):
    # encrypt = key_crypto.encrypt(bytes(str(i), 'utf-8'))
    # encrypt = key_crypto.encrypt(bytes(str('Goôd Morñing Caçamba PíPù ') *i, 'utf-8'))
    encrypt = key_crypto.encrypt(bytes(str(i), 'utf-8'))
    dencrypt = key_crypto.decrypt(encrypt).decode("utf-8")
    percentual = len(encrypt) * 100 / len(dencrypt)
    print('>', 'len encrypt:', len(encrypt), '- type encrypt:', type(encrypt), '- len decrypt:', len(dencrypt), '- type decrypt:', type(dencrypt), '- percentual:', percentual)
    print('>', dencrypt, encrypt, "\n")

print("=" *80)
# ================================================================================
string_to_encrypt = 465464
string_to_encrypt = datetime.datetime.now()
string_to_encrypt = b'Bom Dia Cacamba' # apenas caracteres ASCII
string_to_encrypt = bytes('BöÔm Día Caçãmbà PíPù' *3, 'utf-8')
string_to_encrypt = "BöÔm Día Caçãmbà PíPù " *3
print(type(string_to_encrypt), string_to_encrypt)

encrypt = get_encryption_as_string(string_to_encrypt, key_user="123")
print(type(encrypt), encrypt)

dencrypt = get_decryption_as_string(encrypt, key_user="123")
print(type(dencrypt), dencrypt)