strings = ["a", "abc", "defg", "hi", "jkl"]

for i in strings:
    if len(i) < 3:
        continue
    else:
        print(i)