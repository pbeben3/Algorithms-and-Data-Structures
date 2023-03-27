#nwd iteracja niezoptymalizowana
def NWD(a,b):
    while a!=b:
        if a>b:
            a=a-b
            b=b-a
    return a

print(NWD(12,18))

# nwd rekurencyjnie niezoptymalizowane
def NWDrek(a,b):
    if a!=b:
        if a>b:
            return NWDrek(a-b,b)
        else:
            return NWDrek(a,b-a)
    return a

print(NWDrek(12,18))

#nwd iteracja zoptymalizowana
def nwdII(a,b):
    while b!=0:
        temp = b
        b=a%b
        a=temp
    return a

print(nwdII(12,18))

#nwd rekurencja zoptymalizowana
def nwdIIrek(a,b):
    if b!=0:
        return nwdIIrek(b,a%b)
    return a

print(nwdIIrek(12,18))