side1 = int(input('enter side1:'))
side2 = int(input('enter side2:'))
side3 = int(input('enter side3:'))

if side1 == side2 == side3:
    print('equilateral triangle')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('isosceles triangle')
else:
    print('scalene triangle')
