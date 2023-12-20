d={
    'username':'madhu',
    'password':'madhu@42'
    }
a=input('Enter username:')
b=input('Enter password:')
if a==d['username'] and b==d['password']:
    print('login Successful')
else:
    print('invalid user name or password')