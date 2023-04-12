def Suma(n):
    a=[0]*(n+1)
    for x in range(n+1):
        if x==0 or x==1:
            a[x]=1
        else:
            a[x]=2*a[x-1]-a[x-2]
    return a[n]

print(Suma(50))