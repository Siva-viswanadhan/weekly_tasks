num = int(input("Enter a number: "))
org = num
sum = 0
while num > 0:
    digit = num % 10
    num = num // 10
    sum += digit ** len(str(org))

if org == sum:
    print('number is  armstrong')
else:
    print('number is  not armstrong')
