n = int(input('Podaj ile liczb chcesz wprowadzić: '))
lista = []
for x in range(n):
    lista.append(int(input('')))
lista = sorted(lista,key=lambda x: str(x))
print(lista)