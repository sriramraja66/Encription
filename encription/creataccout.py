from encryptdecrypt import *

def creat_accout():
    u_name = input("Enter The User Name : ")
    u_passwd = input('Enter The Password : ')
    r_passwd = input("Enter The Conform Password : ")
    
    if u_passwd == r_passwd:
        encrypt(u_name,u_passwd)
    else:
        print('Invalid Pass')