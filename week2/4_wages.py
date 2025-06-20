age = int(input('Enter your age: '))
sex = input('enter your sex m or f')

if age >= 18 and age < 30 and sex == 'm' or sex=='M':
    print('your daily wage is 700')
elif age >= 18 and age < 30 and sex == 'f' or sex=='F':
    print('your daily wage is 750')
elif age >= 30 and age <= 40 and sex == 'm'or sex=='M':
    print('your daily wage is 800')
elif age >= 30 and age <= 40 and sex == 'f' or sex == 'F':
    print('your daily wage is 850')
else:
    print('cant get a job')