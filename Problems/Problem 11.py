a = []
for _ in range(20):
    a.append([int(x) for x in input().split(' ')])
max = 0
for i in range(20):
    for j in range(20):
        # Строки и основные диагонали
        if j < 17:
            # Строки
            cur = a[i][j] * a[i][j + 1] * a[i][j + 2] * a[i][j + 3]
            if cur > max:
                max = cur
            # Основные диагонали
            if i < 17:
                cur = a[i][j] * a[i + 1][j + 1] * a[i + 2][j + 2] * a[i + 3][j + 3]
                if cur > max:
                    max = cur
            # Столбцы
            cur = a[j][i] * a[j + 1][i] * a[j + 2][i] * a[j + 3][i]
            if cur > max:
                max = cur
            # Побочные диагонали
            if i > 2:
                cur = a[i][j] * a[i - 1][j + 1] * a[i - 2][j + 2] * a[i - 3][j + 3]
                if cur > max:
                    max = cur
print(max)
