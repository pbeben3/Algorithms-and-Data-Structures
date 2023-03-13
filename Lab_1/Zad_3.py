lista = [1,2,3,4,5,6,7,8,9,10]
n = len(lista)
x = int(input('Podaj x: '))
i =0
while i < n:
    if i < n:
        if x == lista[i]:
            print('Podana wartość występuje w tablicy')
            break
        else:
            i += 1
else:
    print('Podana wartosc nie wystepuje w tablicy ')