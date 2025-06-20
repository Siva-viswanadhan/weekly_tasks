num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
operator = input('enter operator (+,-,*,/): ')

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print('invalid operator')
print('after',operator,',',num1,'and',num2 ,'answer is',result)