with open('../names.txt', 'r') as f:
    s = sorted([x.replace('"', '') for x in f.read().split(',')])
    a = 0
    for i in range(len(s)):
        t = 0
        for j in s[i]:
            t += ord(j.lower()) - 96
        a += t * (i + 1)
    print(a)
