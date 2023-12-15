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

Usando keyring para dados sensíveis do settings.py do Django:
- No Gerenciador de Credencias adicione uma credencial genérica (string) formatada como Json, com os dados que necessitar,
como no exemplo abaixo:
{"NAME":"NAME_DB", "USER":"user_name", "PASSWORD": "password", "HOST": "SERVIDOR\INSTANCIA", "SECRET_KEY": "django_cod_secret_key"}
"""
def credentials(service_name):
    credential_data = {}
    try:
        if keyring.get_credential(service_name, None):
            credential = keyring.get_credential(service_name, None)
            credential_data = ast.literal_eval(credential.password)

        return credential_data
    except keyring.errors.KeyringError as erro_keyring:
        print(f'\nErro no chaveiro! {erro_keyring}\n')
        return credential_data
    except BaseException as e:
        print(f'\nErro! {e}\n')
        return credential_data

service_name = 'aj30'
service = credentials(service_name)
print('service_name', service_name, service.get('HOST', 'host não encontrado'))

