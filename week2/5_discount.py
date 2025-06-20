unit = float(input('enter the unit quantity purchased:'))

cost = unit * 100
print('cost price:',cost)

if cost > 1000:
    cost = cost - (cost * 0.10)
    print('cost price after discount:',cost)