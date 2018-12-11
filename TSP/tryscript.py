import random


def sum_random(n):
    nList = []
    for i in range(10):
        nList.append(random.randrange(n))
    print(nList)
    return sum(nList)


best = 0
for i in range(10):
    current = sum_random(1000)
    best = max(best, current)
    print(current)

print(best)
