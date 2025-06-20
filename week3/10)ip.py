a,b,c,d = map(int,input('enter the ip:').split())

n = int(input ('enter how many ip to print:'))

for i in range(n):
    d += 1
    if d == 256:
        d = 0
        c += 1
        if c == 256:
            c = 0
            b += 1
            if b == 256:
                b = 0
                a += 1
    print(a,b,c,d)