import bcrypt

"""
Fonte: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/

Ver: https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/

Hash de senhas
Para usar o bcrypt, você precisará importar o módulo bcrypt. Depois disso, a função 
bcrypt.hashpw() recebe 2 argumentos: Uma string (bytes) e Salt. 
Salt são dados aleatórios usados ​​na função hash. 
"""

def make_hash_bcrypt(password):
    # convertendo senha em matriz de bytes
    bytes = password.encode('utf-8')
    # gerando o salt
    salt = bcrypt.gensalt()
    print('salt', type(salt), salt)
    # Hashing a senha
    hash = bcrypt.hashpw(bytes, salt)
    return(hash)


def verify_hash_bcrypt(password, hash):
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, hash)
    return result
    

# Hash de senhas 
password1 = 'password123'
password2 = 'passwordabc'
hash1 = make_hash_bcrypt(password1)
print(type(hash1), hash1)
hash2 = make_hash_bcrypt(password2)
print(type(hash2), hash2)
  
# Verificando senhas
# Os exemplos a seguir verificam uma senha em relação a um valor de hash.
  
password1 = 'password000' # senha incorreta
password2 = 'passwordabc' # senha correta 

# checking password
result1 = verify_hash_bcrypt(password1, hash1)
print(result1)
result2 = verify_hash_bcrypt(password2, hash2)
print(result2)