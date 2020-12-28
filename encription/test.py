from cryptography.fernet import Fernet
key = Fernet.generate_key()

f = Fernet(key)
s = 'sriram'
token = f.encrypt(f'{s}')

print(token)

for i in f.decrypt(token): 
    print(chr(i),end='')