from cryptography.fernet import Fernet
import os

# Fonte: https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/

# # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# keyring
# veja https://jobu.com.br/2021/06/26/como-esconder-uma-senha-em-um-script-python/
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

homepath = os.environ['HOMEPATH']
filename = 'txt_sig_abs'
# =============================================================================
key = Fernet.generate_key() 
print('1', key)
# =============================================================================
# O trecho de código a seguir cria uma senha criptografada usando a chave (variável key) 
# iniciada anteriormente.
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY=' 
cipher_suite = Fernet(key) 
ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword") #necessário ser bytes 
print('2', ciphered_text)
# =============================================================================
# O ciphered_text retornado da instrução print acima é o que iremos escrever posteriormente 
# em um arquivo binário. Antes de fazer isso, vamos validar que podemos retornar 
# a senha previamente criptografada com a seguinte declaração:
# =============================================================================
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY=' 
cipher_suite = Fernet(key) 
ciphered_text = b'gAAAAABaHvk3g8IG4cln7g5HCulppy1bAPVuhtskVcgPXRyytx6RkIqjcI0mAMA7Oy_ 56T6J0dk-yjxI_WlZtjxnUBbR-EvoQa_oqCKoQJFbv_uc2WdXMSI=' 
unciphered_text = (cipher_suite.decrypt(ciphered_text)) 
print('3', unciphered_text)
# =============================================================================

# Gravar senha criptografada em arquivo binário
# Agora que temos a senha criptografada como um byte literal, podemos armazenar esse objeto em um arquivo. 
# Em Python, devemos se lembrar que gravar em um arquivo de texto grava o texto, mas apenas se 
# for realmente texto. Embora o objeto retornado acima possa parecer um texto, não é. É um byte literal 
# e precisará ser convertido em uma string (UTF-8) para ser gravado em um arquivo de texto ou, 
# como veremos, gravar o byte literal em um arquivo binário. O código a seguir usa a chave 
# gerada anteriormente, cria uma senha criptografada e grava esse resultado literal de 
# byte em um arquivo binário.
# =============================================================================
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY=' 
cipher_suite = Fernet(key) 
ciphered_text = cipher_suite.encrypt(b'SuperSecretpassword') 
with open(f'{homepath}\{filename}.bin', 'wb') as file_object : file_object.write(ciphered_text)
# =============================================================================
# Recupere a senha criptografada e descriptografe
# Com os dados agora gravados em um arquivo binário, vamos recuperar a senha criptografada e usar 
# a chave gerada anteriormente para descriptografá-la. Essencialmente, trabalhando ao contrário 
# de onde começamos. Vamos começar recuperando a senha criptografada. 
with open(f'{homepath}\{filename}.bin', 'rb') as file_object: 
    for line in file_object: 
        cryptedpwd = line 
print('4', cryptedpwd)
# Levando isso adiante, pegamos a senha criptografada, usamos a biblioteca de criptografia 
# para descriptografá-la e finalmente a convertemos de volta em uma string.
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
print('>>>>\nhomepath', homepath)
with open(f'{homepath}\{filename}.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #Convert para string
print('5', plain_text_encryptedpassword)