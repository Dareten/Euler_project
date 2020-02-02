import timeit

a = timeit.default_timer()
x, y = 0, 0
for i in range(1, 101):
    x += i**2
    y += i
print(y**2 - x)
print(timeit.default_timer() - a, end='')
