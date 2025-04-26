import random

l = [0, 2, 3, 5]
print(random.choice(l))
print(random.seed(0))
print(random.choice(l))

l.append([0,1])
if [0, 1] in l:
    print(l[4])
print(l)