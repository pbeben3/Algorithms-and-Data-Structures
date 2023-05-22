
def binarySearch(lista,x):
    m=0
    h=len(lista)-1
    l=0
    while l<=h:
        m=(h+l)//2
        if lista[m]<x:
            l=m+1
        elif lista[m]>x:
            h=m-1
        else:
            return f"{x} występuje w tablicy"

    return f"{x} nie występuje w tablicy"



from random import randint
lista = []
for  x in range (0,20):
    lista.append(randint(-100,100))

print(lista)
lista.sort()
print(lista)

print(binarySearch(lista,3))
