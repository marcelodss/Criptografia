import os
from pathlib import Path
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

def get_path_file():
    try:
        path_end = 'hash'
        file = f"sigpec.bin"
        path = str(os.environ['HOMEPATH']) + "\\" + path_end
        return {'path': path, 'file': file}
    except BaseException as e:
        cwd = Path.cwd()
        print(f'Erro! {e}')
        return {'path': Path.joinpath(cwd, path_end), 'file': file}

def get_key_fernet(key_user=None):
    try:
        if key_user == None or key_user == "":
            path_file = get_path_file()
            if os.path.exists(path_file['path']) == False:
                os.mkdir(path_file['path'])

            if os.path.exists(f"{path_file['path']}\{path_file['file']}") == False:
                key = Fernet.generate_key()
                with open(f"{path_file['path']}\{path_file['file']}", 'wb') as f: 
                    f.write(key)
            else:
                with open(f"{path_file['path']}\{path_file['file']}", 'rb') as f:
                    key = f.read()
        else:
            key_user = str(key_user)
            char = key_user[-1]
            char = bytes(char, "utf-8")
            code_bytes = bytes(key_user, "utf-8")
            key = urlsafe_b64encode(code_bytes.ljust(32, char)[:32])
            # ljust(32) preenche os bytes de senha com bytes nulos (ou char) para garantir que 
            # a chave tenha 32 bytes de comprimento. Em seguida, [:32] trunca a chave para 
            # 32 bytes se for maior que isso. Por fim, a chave é codificada usando 
            # base64.urlsafe_b64encode() para obter uma chave codificada em base64 segura para URL.
        return Fernet(key)
    except BaseException as e:
        print(f'Erro! {e}')

def get_encryption_as_string(string, key_user=None):
    try:
        key_fernet = get_key_fernet(key_user)
        return key_fernet.encrypt(bytes(str(string), 'utf-8')).decode('utf-8')
    except BaseException as e:
        print(f'Erro! {e}')
        return None
def get_decryption_as_string(code, key_user=None):
    try:
        key_fernet = get_key_fernet(key_user)
        return key_fernet.decrypt(code).decode('utf-8')
    except BaseException as e:
        print(f'Erro! {e}')
        return None