def najwieksza(a, start, koniec):
    if start == koniec:
        maximum = a[start]
        return (maximum)
    elif start + 1 == koniec:
        if a[start] > a[koniec]:
            maximum = a[start]
        else:
            maximum = a[koniec]
        return (maximum)
    else:
        srodek = int((start + (koniec - start) / 2))
        max_l = najwieksza(a, start, srodek)
        max_p = najwieksza(a, srodek + 1, koniec)
    return (max(max_l, max_p))

a = [1,8,19,20,35,14,7]
koniec = len(a)-1
start = 0
print(f'Maksymalna wartoscia w wektorze to: {najwieksza(a, start, koniec)}')