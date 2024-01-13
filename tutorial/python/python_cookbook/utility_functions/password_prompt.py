import getpass

user = getpass.getuser()
passwd = getpass.getpass()

def user_login(user, passwd):
    if user == 'riaz' and passwd == 'riaz':
        return True
    else:
        return False

if user_login(user, passwd):
    print('Authenticated')
else:
    print('Try Again')