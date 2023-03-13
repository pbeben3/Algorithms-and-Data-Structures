import numpy as np
tablica_2 = np.array([[2,6,8,1,4],[5,8,10,3,20]])
k = int(input('Podaj liczbę kolumn: '))
w = int(input('Podaj liczbę wierszy: '))

for i in range(w):
    min = tablica_2[i][0]
    for j in range(k):
        if tablica_2[i][j] < min:
            min = tablica_2[i][j]
            pom = tablica_2[i][0]
            tablica_2[i][0] = min
            tablica_2[i][j] = pom
    print(f'wartosc minimalna w wierszu {i} = {min} ')
print(tablica_2)