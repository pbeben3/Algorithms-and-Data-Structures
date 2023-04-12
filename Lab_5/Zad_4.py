def ws_dw(n, m):
    a = [[0 for x in range(m + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, m) + 1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

    return a[n][m]

n = int(input('Podaj n: '))
m = int(input('Podaj m: '))
print(f'{n} nad {m} = {ws_dw(n,m)}')