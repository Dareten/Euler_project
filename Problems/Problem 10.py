from math import sqrt

n = 2000000
s = set(range(3, n, 2))
for i in range(2, int(sqrt(n))):
    if i in s:
        s -= set(range(i ** 2, n, i))
print(sum(s) + 2)
