lst = [12, 5, -3, 18, 0, -7, 25, -1, 9]
sum = 0

for i in lst:
    if i < 0:
        continue
    else:
        sum += i
print(sum)