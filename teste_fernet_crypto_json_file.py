import json 
from modulos.access_key_fernet import get_encryption_as_string, get_decryption_as_string

"""
Existem vários módulos para codificar e decodificar JSON em Python. Os dois módulos mais populares 
são json e simplejson. O módulo json é um pacote embutido na biblioteca padrão do Python, o que 
significa que podemos usá-lo imediatamente sem precisar instalá-lo.
"""

"""
A serialização é o processo de conversão de objetos Python — na maioria dos casos, um dicionário — em dados 
ou string formatados em JSON. Ao serializar, os tipos Python são codificados para um equivalente JSON. O 
módulo json fornece dois métodos — json.dump() e json.dumps() — para serializar objetos Python para o formato JSON.

- json.dump() é usado ao escrever o equivalente JSON de objetos Python em um arquivo.
- json.dumps() (com um “s”) é usado ao converter um objeto Python em uma string formatada em JSON.
"""

senha_to_encrypt = "minha senha muuuito longa %âêÎçÇö " *3
senha_encrypted =  get_encryption_as_string(senha_to_encrypt)

print('senha_encrypted', type(senha_encrypted), senha_encrypted)

dictionary = { 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500",
    "list": ["", '4', -4, 4, 'quatro', 0.4],
    "tuple": ["", '5', -5, 5, 'cinco', 0.5],
    "dict": {"num": [-1, 0, 1, 2, 3], 'carac': ("", 'abc', 'def', 'ghi' )},
    "none": None,
    "vazio": "",
    "boolean": True,
    'senha': senha_encrypted
} 

# =============================================================================
with open("json_dumped.json", "w", encoding='utf-8') as outfile: 
    json.dump(dictionary, outfile, indent=4) 
# =============================================================================
json_dumpeds = json.dumps(dictionary, indent=4) 
with open("json_dumpeds.json", "w", encoding='utf-8') as outfile: 
    outfile.write(json_dumpeds) 
# Conforme declarado anteriormente, o método json.dumps() é usado para converter objetos 
# Python em uma string formatada em JSON. Podemos ver no console que nossos dados JSON são do tipo str
print('\n>>>json_dumpeds tipo: ', type(json_dumpeds), '\n')

# =============================================================================
"""
A desserialização de JSON é o processo de decodificação de objetos JSON para objetos Python equivalentes 
ou tipos Python. Podemos converter dados formatados em JSON em objetos Python usando dois 
métodos — json.load() e json.loads() — que são fornecidos pelo módulo json.

- json.load()é usado ao ler dados formatados em JSON de um arquivo.
- json.loads()(com um “s”) é usado ao analisar uma string JSON para um dicionário Python.
"""
# =============================================================================
with open('json_dumped.json', 'r', encoding='utf-8') as openfile: 
    json_load = json.load(openfile) 
print('\n>>>json_load tipo:', type(json_load),'\n') 
print('\n>>>json_load: ', json_load) 
# =============================================================================
json_loads = json.loads(json_dumpeds)
print('\n>>>json_loads tipo:', type(json_loads),'\n') 
print('\n>>>json_loads: ', json_loads) 

senha_decrypted = get_decryption_as_string(json_loads['senha'])
print("\n", '*'*10, "\n senha_decrypted", type(senha_decrypted), senha_decrypted)