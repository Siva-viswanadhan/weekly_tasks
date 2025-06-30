for i in range(1,5):
    for j in range(5-i):
        print(' ',end = ' ')
    for k in range(1,i+1):
        print(k,end = ' ')
    for k in range(i-1,0,-1):
        print(k,end = ' ')
    print()