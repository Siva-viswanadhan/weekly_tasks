for i in range(1,100):
    for j in range(1,100):
        if i*j <10:
            continue
        print(i,j)
        break
    # else:
    #     continue
    break