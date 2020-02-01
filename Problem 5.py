import timeit

a = timeit.default_timer()
prost, x = (3, 7, 11, 13, 17, 19), 20
for i in prost:
    x *= i
num = x
q = True
while q:
    t = 0
    for i in range(11, 20):
        t += num % i
        if t != 0:
            break
    if t == 0:
        q = False
        break
    num += x  # Так как на 20 без остатка делятся только двадцатки
print(num)
print(timeit.default_timer() - a, end='')
