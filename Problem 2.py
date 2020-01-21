import timeit

a = timeit.default_timer()
f, i = [1, 2], 2
while f[-1] < 4000000:
    f.append(f[i - 1] + f[i - 2])
    i += 1
res = sum(filter(lambda x: x % 2 == 0 and x < 4000000, f))
print(res)
print(timeit.default_timer() - a)
