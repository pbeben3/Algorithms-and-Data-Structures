def zamiana(n):
    if n >= 1:
        zamiana(n // 2)
    print(n % 2,end = '')

zamiana(10)