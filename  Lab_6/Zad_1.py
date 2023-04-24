zle=0
for x in range(3):
    pin=int(input('Podaj PIN: '))
    if pin==5010:
        print('zalogowano pomyślnie')
        break
    else:
        zle+=1

if zle==3:
    print('zablokowano karte')