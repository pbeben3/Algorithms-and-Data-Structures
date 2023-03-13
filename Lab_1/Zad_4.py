lista = [1,6,34,123,2,1,-7,7,89]
min = lista[0]
n = (len(lista))
for x in range(n):
    if x < n:
        if lista[x] < min:
            min = lista[x]
print(f'Minimalna wartosc w tablicy to {min}')
