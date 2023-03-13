import math
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

if a != 0:
    delta = (b*b) - 4*(a*c)
    print(delta)
    if delta > 0:
        x1 = (-b-(math.sqrt(delta))) / (2*a)
        x2 = (-b+(math.sqrt(delta))) / (2*a)
        print(f'x1 = {x1} x2 = {x2}')
    else:
        if delta == 0:
            x1 = (-b) / (2*a)
            print(f'x1 = {x1}')
        else:
            print('Brak rzeczywistych rozwiązań')

else:
    print('To nie jest równanie kwadratowe')