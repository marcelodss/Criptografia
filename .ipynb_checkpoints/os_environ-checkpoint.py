import os, traceback
print(os.getlogin())
print(os.getenv("HOME"))

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

os.environ['path']

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')
print(USER, PASSWORD)

# Getting non-existent keys
FOO = os.getenv('FOO') # None
BAR = os.environ.get('BAR') # None
print(FOO, BAR)
# BAZ = os.environ['BAZ'] # KeyError: key does not exist.

for key in os.environ:
    print(key, '=>', os.environ[key])

print('\n>>>>', os.environ['TEMP'])
try:
    print('\n>>>>', os.environ['ExVar1'])
except BaseException as e:
    print(f'\nErro\n: {traceback.format_exc()}')

print('\n>>> relpath', os.path.dirname(os.path.relpath(__file__)))
print('\n>>> realpath', os.path.dirname(os.path.realpath(__file__)))