import random

numb = []
num = random.randint(0, 15)

try:
    while num != 0:
        numb.append(num)
        num = random.randint(0, 15)

except IndexError:
    print("The list is full")

for i in numb:
    print(i)
