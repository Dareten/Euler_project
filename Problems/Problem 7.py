import timeit
from config import issimple


a = timeit.default_timer()
n = 5
s = [2, 3]
while True:
    if issimple(n, s):
        s.append(n)
    if len(s) == 10001:
        break
    n += 2
print(s[-1])
print(timeit.default_timer() - a, end='')
