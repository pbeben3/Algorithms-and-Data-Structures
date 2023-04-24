def srednia(tablica):
    suma = 0
    for x in range(len(tablica)):
        suma = suma+tablica[x]
    srednia=suma/len(tablica)
    return srednia

tablica = [2,2,2,4]
print(srednia(tablica))
