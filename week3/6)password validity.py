password = input('enter password :')
valid = False
for i in password:
    if i.isdigit():
        valid = True
        break

if valid and len(password) >= 8:
    print('password is valid')
else:
    print('password is invalid')