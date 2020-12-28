from general import *
from cryptography.fernet import Fernet

def gen_key():
    key = Fernet.generate_key()
    with open('Keys.key','wb') as key_file:
        key_file.write(key)

def lod_key():
    f = open('Keys.key','rb').read()
    return f

def encrypt(name,passwd):
    key =lod_key()
    encode_name = name.encode()
    encode_pass = passwd.encode()
    f = Fernet(key)
    encrypted_name= f.encrypt(encode_name)
    encrypted_pass= f.encrypt(encode_pass)
    file_name = name+'.txt'
    file_name_pass = name+'1.txt'
    with open(file_name,'wb') as file:
        file.write(encrypted_name)
    with open(file_name_pass,'wb') as file_pass:
        file_pass.write(encrypted_pass) 
    print('Account Created Please Restart The Engine....')    

def decrypt(name,passwd):
    key = lod_key()
    f = Fernet(key)
    file_name = name+'.txt'
    file_name_pass = name+'1.txt'
    u_name_file = open(file_name,'rb').read()
    u_pass_file = open(file_name_pass,'rb').read()
    user_name = f.decrypt(u_name_file)
    user_pass = f.decrypt(u_pass_file)  
    
    u_name = user_name.decode()
    u_pass = user_pass.decode()
    
    if u_name == name and u_pass == passwd:
        print('Account Info... Is Updatating...')
    else:
        print('Invalid User Name And Password..')    
        
    