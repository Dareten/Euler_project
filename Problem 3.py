import timeit
from config import primfacs


a = timeit.default_timer()
num = 600851475143
print(int(sorted(primfacs(num))[-1]))
print(timeit.default_timer() - a, end='')

