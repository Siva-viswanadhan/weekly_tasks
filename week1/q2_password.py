password = input('Enter password: ')


char_digit = False

for char in password:
    if  char.isdigit():
        char_digit = True
        break

if len(password) >= 8 and char_digit:
    print('Password is valid')
else:
    print('Password is invalid')