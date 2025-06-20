def permute(num):
    if len(num) == 0:
        return[[]]
    result = []

    for i in range(len(num)):
        rest = num[:i] + num[i+1:]
        for p in permute(rest):
          result.append(p + [num[i]])
    return result

print(permute([1,2,3]))