import secrets
import hashlib

secrets_bytes = secrets.token_bytes(20)
print('\n>>> secrets_bytes', secrets_bytes)
secrets_bytes = secrets.token_bytes()
print('\n>>> secrets_bytes', secrets_bytes)

secrets_hex = secrets.token_hex(20)
print('\n>>> secrets_hex', secrets_hex)
secrets_hex = secrets.token_hex()
print('\n>>>', secrets_hex)

secrets_urlsafe = secrets.token_urlsafe(20)
print('\n>>>', secrets_urlsafe)
secrets_urlsafe = secrets.token_urlsafe()
print('\n>>>', secrets_urlsafe)

for i in range(10):
    print("\n x x x > ", secrets.token_urlsafe())

data = secrets_bytes
hash_object = hashlib.sha256(data)
hash_value = hash_object.hexdigest()
print(hash_value)

data = secrets_bytes
hash_object = hashlib.sha256(data)
hash_value = hash_object.hexdigest()
print(hash_value)