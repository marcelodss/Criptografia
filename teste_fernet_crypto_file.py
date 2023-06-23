import os
from pathlib import Path

from modulos.access_key_fernet import get_key_fernet

file = Path(os.path.dirname(os.path.realpath(__file__)), 'data_source', 'nba.txt')
key_crypto = get_key_fernet()

# ==== Criptografando Arquivo==================================================
# Abrindo o arquivo original para criptografar
with open(str(file), 'rb') as f:
    original = f.read()
# criptografar o arquivo
encrypted = key_crypto.encrypt(original)
# Abrindo o arquivo no modo de gravação e
# escrevendo os dados criptografados
with open(str(file )+ '_crypt', 'wb') as f:
    f.write(encrypted)
print('\n', '='*100,  '\n', f'{file}_crypt', "\ncriptografado...")

# ==== Descriptografando Arquivo===============================================
# Abrindo o arquivo criptografado
with open(str(file) + '_crypt', 'rb') as f:
    encrypted = f.read()
 # descriptografando o arquivo
decrypted = key_crypto.decrypt(encrypted)
 # Abrindo o arquivo no modo de gravação e
# escrevendo os dados descriptografados
with open(str(file) + '_decrypt', 'wb') as f:
    f.write(decrypted)
print('\n', '='*100,  '\n', f'{file}_decrypt', "\ndescriptografado...")