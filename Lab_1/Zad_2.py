lista = []
n = int(input('Podaj liczbę elementów do wczytania: '))
while n<0:
    n = int(input('Podaj liczbę elementów do wczytania: '))
ile_u = 0
for x in range(n):
    lista.append(int(input('Podaj liczbę: ')))
    if lista[x] < 0:
        ile_u += 1
print(f'Występuje {ile_u} liczb ujemnych')
