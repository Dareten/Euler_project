import timeit
from config import number_8


a = timeit.default_timer()
max_elem = 0
q = [int(x) for x in str(number_8)]
for i in range(len(q) - 13):
    t = 1
    for j in range(13):
        t *= q[i + j]
    max_elem = t if max_elem < t else max_elem
print(max_elem)
print(timeit.default_timer() - a, end='')
