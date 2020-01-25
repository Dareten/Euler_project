def issimple(num, arr):
    for i in arr:
        if num % i == 0:
            return False
    return True


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i += 1
    if n > 1:
        primfac.append(n)
    return primfac
