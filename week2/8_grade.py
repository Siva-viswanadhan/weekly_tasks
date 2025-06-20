mark = int(input('mark: '))

if mark > 80 and mark <= 100:
    print('grade is A')
elif mark <= 80 and mark > 60:
    print('grade is B')
elif mark <=60 and mark > 50:
    print('grade is C')
elif mark <= 50 and mark > 45 :
    print('grade is D')
elif mark <=45 and mark > 25 :
    print('grade is E')
elif mark <= 25 and mark >= 0:
    print('grade is F')
else :
    print('enter correct marks')
