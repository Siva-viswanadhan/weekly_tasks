import random
import string


length = int(input('Enter length of identifier: '))
count = int(input('Enter count of identifier: '))

first_chars = string.ascii_letters + "_"
second_chars = string.ascii_letters + "_"+string.digits


generated = set()
while len(generated) < count:
    if length==1:
        identifier = random.choice(first_chars)
    else:
        identifier = random.choice(first_chars)

        for i in range(length-1):
            identifier += random.choice(second_chars)


    if identifier not in generated:
        generated.add(identifier)
        print(identifier)