from passlib.context import CryptContext

"""
Fonte: https://jobu.com.br/2021/06/26/como-esconder-uma-senha-em-um-script-python/

Ver: https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/
"""

"""
O hash é diferente da criptografia porque a criptografia funciona como um método bidirecional. 
Qualquer senha criptografada pode ser descriptografada. O hash, por outro lado, funciona mapeando 
um valor (como uma senha) para um novo valor embaralhado. Idealmente, não deve haver uma maneira de 
mapear o valor / senha com hash de volta ao valor / senha original.
"""

"""
Configurando um objeto CryptContext
Primeiro, para fazer isso, precisamos decidir qual algoritmo de hash queremos usar. Existem várias 
possibilidades aqui, mas várias são especificamente recomendadas pela biblioteca passlib:
argon2bcryptpbkdf2_sha256pbkdf2_sha512sha256_cryptsha512_crypt

Alguns desses algoritmos requerem a instalação de pacotes adicionais. Se você tentar usá-los sem 
essas dependências, receberá uma mensagem solicitando a instalação de alguns pacotes primeiro. 
Por exemplo, o pacote argon2_cffi é necessário para usar o algoritmo argon2 acima.

Em segundo lugar, também precisamos especificar o número de “rodadas”. Uma rodada é uma coleção 
de operações que formam uma função. Esta função é então executada várias vezes para mapear nossa 
senha para uma versão em hash. Um número menor de rodadas significará que tudo o que você está 
fazendo hash não é tão seguro porque menos operações estão sendo realizadas para embaralhar as informações. 
No entanto, um número maior de rodadas levará mais tempo para concluir a operação de hash. O 
número de rodadas a serem escolhidas também depende do algoritmo que você escolher. A 
escolha do número de rodadas para fins de segurança tem a ver principalmente com a lentidão, 
ou seja, se for rápido para gerar um hash, também é mais rápido descobrir o valor original por força bruta. 
Algoritmos como bcrypt e argon2 são mais lentos para produzir valores hash e, portanto, geralmente 
considerados mais seguros.
"""


to_hash = "test_password"

# create CryptContext object
context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=50000
)

# hash password
print(context.hash(to_hash))

"""
Neste primeiro exemplo, estamos usando o algoritmo PBKDF2-SHA256, pois essa é uma escolha comum e 
normalmente funciona sem problemas em diferentes sistemas operacionais. Uma vez que o objeto CryptContext 
é criado, podemos hash nossa senha usando o método hash como acima.

Para verificar se uma senha corresponde ao hash correspondente, podemos usar o método de verificação. 
O método de verificação não “descompõe” a senha com hash, mas, em vez disso, faz o hash da senha desprotegida 
e a compara com a versão com hash.
"""

hashed_password = context.hash(to_hash)
print(context.verify(to_hash, hashed_password))

# =============================================================================

"""
A seguir, vejamos outro exemplo. Desta vez, usaremos o algoritmo argon2. 
Como mencionado acima, precisamos primeiro instalar o pacote argon2_cffi para isso. argon2 
é um algoritmo relativamente mais recente que foi projetado especificamente para hash de senhas.
"""

context = CryptContext(
        schemes=["argon2"],
        default="argon2",
        argon2__default_rounds=100 #1000
)

# hash password
print(context.hash(to_hash))
hashed_password = context.hash(to_hash)
print(context.verify(to_hash, hashed_password))

"""Argon2 é uma função de hashing de senha que foi selecionada como a 
vencedora do Password Hashing Competition (PHC) em 2015. Ele foi projetado 
para ser resistente a ataques como ataques de dicionário, ataques de força bruta 
e ataques de pré-computação."""

