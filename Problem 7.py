import timeit
import math


def issimple(num, arr):
    for i in arr:
        if num % i == 0:
            return False
    return True


a = timeit.default_timer()
n = 5
s = [2, 3]
while True:
    if issimple(n, s) is True:
        s.append(n)
    if len(s) == 10001:
        break
    n += 2
print(s[-1])
print(timeit.default_timer() - a)
