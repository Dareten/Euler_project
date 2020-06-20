a = []
for _ in range(15):
    a.append([int(x) for x in input().split()])
for i in range(13, -1, -1):
    for j in range(len(a[i])):
        if a[i+1][j] >= a[i+1][j+1]:
            a[i][j] += a[i+1][j]
        else:
            a[i][j] += a[i+1][j+1]
print(a[0][0])
