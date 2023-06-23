import os
from dotenv import load_dotenv, dotenv_values

"""
Carregando como variável de ambiente
O pacote dotenv fornece um método load_dotenv() que lê o arquivo fornecido como um caminho de arquivo. 
Se nenhum caminho for especificado, ./.env será usado como o caminho padrão, o que significa que ele 
procurará o arquivo  .env no diretório de script Python.
"""
load_dotenv('.env.development')
print(os.getenv('SERVIDOR')) 
print(os.getenv('INSTANCIA'))
print(os.getenv('DRIVER'))

"""
Carregando como um dicionário
Usando esse método, as variáveis ​​de ambiente não são afetadas. Em vez disso, eles são analisados ​​
e convertidos em um dicionário Python."""
config = dotenv_values(".env.development")
print(config['SERVIDOR'])
print(config['INSTANCIA'])
print(config['DRIVER'])

"""Variáveis ​​de ambiente de controle de versão
Um projeto pode ter várias instâncias, como teste, desenvolvimento, preparação ou produção. 
Ao usar instâncias diferentes, diferentes variáveis ​​de ambiente podem ser necessárias. 
Portanto, para resolver esse problema, um projeto pode usar vários arquivos .env como:

.env.shared
.env.development
.env.production

A segregação de variáveis ​​em arquivos diferentes pode nos permitir controlar a versão dos arquivos de ambiente.
"""