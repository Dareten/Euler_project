max, ans = 9, 12
for i in range(999999, 12, -2):
    c, n = 1, i
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        c += 1
        n = int(n)
    if c > max:
        max = c
        ans = i
print(ans, max)
