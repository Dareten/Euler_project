def factor(n):
    res = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        res.append(n)
    return res

ii = 2
number = 3
while True:
    primes = factor(number)
    answer, num, actual, length = 1, 1, primes[0], len(primes)
    for i in range(1, length):
        if primes[i] == actual:
            num += 1
        else:
            answer *= num + 1
            num = 1
            actual = primes[i]
    answer *= num + 1
    if answer > 500:
        print(number)
        break
    ii += 1
    number += ii
