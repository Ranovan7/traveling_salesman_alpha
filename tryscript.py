import random


def sum_random(n):
    nList = []
    for i in range(10):
        nList.append(random.randrange(n))
    print(nList)
    return sum(nList)
