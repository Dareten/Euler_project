def find_divisors(n) :
    i = 1
    a = []
    while i <= n // 2 + 1 :
        if not n % i:
            a.append(i)
        i += 1
    return(sum(a))
arr = [False for i in range(1, 10000)]
q = set()
for i in range(len(arr)):
    if not arr[i]:
        t = find_divisors(i)
        if t < 10000 and not arr[t]:
            tt = find_divisors(t)
            if i == tt and i != t:
                q.add(t)
                q.add(tt)
print(sum(q))
