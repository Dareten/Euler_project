import timeit


a = timeit.default_timer()
q, s = False, []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if i * j == int(str(i * j)[::-1]):
            s.append(i * j)
print(max(s))
print(timeit.default_timer() - a, end='')

