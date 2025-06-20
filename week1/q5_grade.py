sub1 = int(input('Enter subject 1 marks: '))
sub2 = int(input('Enter subject 2 marks: '))
sub3 = int(input('Enter subject 3 marks: '))
sub4 = int(input('Enter subject 4 marks: '))

average = (sub1 + sub2 + sub3 + sub4) / 4
print('Average:', average)

if average >= 90:
    print('Grade is A+')
elif average >= 80:
    print('Grade is A')
elif average >= 70:
    print('Grade is B+')
elif average >= 60:
    print('Grade is B')
elif average >= 50:
    print('Grade is C')
elif average >= 40:
    print('Grade is P')
else:
    print('You failed in the exam')
