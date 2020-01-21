import timeit


a = timeit.default_timer()
q, s = [], 0
for i in range(3, 1000):
    if i % 3 == 0:
        s += i
        q.append(i)
    elif i % 5 == 0 and i not in q:
        s += i
        q.append(i)
print(s)
print(timeit.default_timer() - a)
