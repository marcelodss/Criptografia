import getpass, keyring 
from keyring.backends import Windows
keyring.set_keyring(Windows.WinVaultKeyring())
import ast

"""
pypi: https://pypi.org/project/keyring/
Fonte: https://jobu.com.br/2021/06/26/como-esconder-uma-senha-em-um-script-python/
veja: 
https://stackoverflow.com/questions/14756352/how-is-python-keyring-implemented-on-windows
https://techjogging.com/store_sensitive_data_locally_windows_using_python.html

"""
def create_keyring(service_name):
    print('='*12, 'informe usuário e senha', '='*12)
    username = input("Username: ")
    password = getpass.getpass()
    keyring.set_password(service_name, username, password)


def delete_keyring(service_name, user_name):
    keyring.delete_password(service_name, user_name)

""""
Usando keyring para dados sensíveis do settings.py do Django:
- No exemplo abaixo, os dados são gravados no gerenciador como uma string formatada como Json:
{"NAME":"NAME_DB", "USER":"user_name", "PASSWORD": "password", "HOST": "SERVIDOR\INSTANCIA", "SECRET_KEY": "django_cod_secret_key"}
"""

try:
    service_name = "service_name"
    if not keyring.get_credential(service_name, None):
        print(f"service name {service_name} não existe no gerenciador de senhas." )
    else:
        credential = keyring.get_credential(service_name, None)
        uid=credential.username
        pwd=credential.password
        aj30 = ast.literal_eval(pwd)
        print(type(aj30['HOST']))

except keyring.errors.KeyringError as erro_keyring:
    print(f'\nErro no chaveiro! {erro_keyring}\n')
    # delete_keyring(service_name, uid)
except BaseException as e:
    print(f'\nErro! {e}\n')
    # delete_keyring(service_name, uid)
