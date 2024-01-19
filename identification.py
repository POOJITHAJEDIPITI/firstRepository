db={'username':'RAHUL','password':'rahul123'}
username=eval(input('enter your username\n'))
password=eval(input('enter your password\n'))
if username==db['username'] and password==db['password']:
    print('sucessfully logged in')
else:
    print('invalid username & password')
