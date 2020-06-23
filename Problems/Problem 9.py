from config import is_abc

f = True
for i in range(2, 999):
    if not f:
        break
    for j in range(2, i):
        if not f:
            break
        k = 1000 - i - j
        if is_abc(k, j, i) and f and k < j:
            print(k * j * i)
            f = False
            break
