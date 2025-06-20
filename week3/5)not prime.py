lower_limit = int(input('lower limit: '))
upper_limit = int(input('upper limit: '))
for i in range(lower_limit, upper_limit + 1):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1

    if flag == 1:
        print(i)