from general import *
from currentaccount import current_account
from creataccout import creat_accout
def Display():   
    print('''
          1.Create Account
          
          2.Current Account
          
          3.Exit
          
          ''')
mode = True
while mode:
    cls()
    Display()    
    opt = input('Enter The Option (1/2/3) : ')
    ch = int(opt)

    if ch == 1:
        cls()
        creat_accout()
        op = input('Did You Want To Continue (Y/N): ')
        if op == 'y' or op == 'Y':
            mode = True
        else:
            mode = False    
            
    elif ch == 2:   
        cls()
        current_account()
        op = input('Did You Want To Continue (Y/N): ')
        if op == 'y' or op == 'Y':
            mode = True
        else:
            mode = False 
            
    elif ch == 3:   
        print('Have A Nice Day.....')
        mode = False
    else:
        print('Invalid Option...')
        mode = False