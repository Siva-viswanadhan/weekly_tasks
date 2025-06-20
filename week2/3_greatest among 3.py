num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = int(input('Enter a third number: '))

if num1 > num2 and num1 > num3 :
    print(num1,'is greatest num1')
elif num2>num1 and num2>num3 :
    print(num2,'is greatest num2')
elif num3>num1 and num3>num2 :
    print(num3,'is greatest num3')
else:
    print('cant find')