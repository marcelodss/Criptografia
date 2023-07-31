import pyodbc, getpass
import keyring 
from dotenv import dotenv_values
from keyring.backends import Windows
keyring.set_keyring(Windows.WinVaultKeyring())

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

try:
       service_name = "keyring Python"
       if not keyring.get_credential(service_name, None):
              create_keyring(service_name)

       credential = keyring.get_credential(service_name, None)
       uid=credential.username
       pwd=credential.password

       database = dotenv_values(".env.development")
       driver = database['DRIVER']
       server = f"{database['SERVIDOR']}\{database['INSTANCIA']}"
       conn = pyodbc.connect('Driver={' + driver + '};Server=' + server + ';DATABASE=master' + '; Uid=' + uid + ';Pwd=' + pwd +'; fast_executemany=True; Encrypt=no;')
       cur = conn.cursor() 

       listOfTables = cur.execute(
       f"""SELECT name FROM master.sys.tables; """).fetchall()
       if listOfTables:
              print('-'*50, '\n', f'sys.tables existe em master.', '\n', '-'*50)
       else:
              print('-'*50, '\n', f'sys.tables não existe em master.', '\n', '-'*50)

       cur.close()
       conn.close()
except pyodbc.Error as erro_pyodbc:
       print(f'\nErro na conexão! {erro_pyodbc}\n')
       delete_keyring(service_name, uid)
       create_keyring(service_name)
except keyring.errors.KeyringError as erro_keyring:
       print(f'\nErro no chaveiro! {erro_keyring}\n')
       delete_keyring(service_name, uid)
except BaseException as e:
       print(f'\nErro! {e}\n')
       delete_keyring(service_name, uid)
finally:
       conn = None
       cur = None
