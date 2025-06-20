string = input("Enter a string: ")

if string == '':
    print('it is not a valid identifier')
elif not (string[0].isalpha() or string[0] == '_'):
    print('it is not a valid identifier')
else:
    valid = True
    for char in (string[1:]):
        if not char.isalnum() or char == '_':
            valid=False
            break


    if valid:
        print('it is a valid identifier')
    else:
        print('it is not a valid identifier')