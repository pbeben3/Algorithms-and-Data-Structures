def suma(A):
    n=len(A)
    if n==0:
        return 0
    if n==1:
        return A[0]
    s=n//2
    l=A[:s]
    p=A[s:]
    s_l=suma(l)
    s_p=suma(p)
    return s_l+s_p

A=[5,6,8,1,4,3,3,]
print(suma(A))


