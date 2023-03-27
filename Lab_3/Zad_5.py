def wieza(n,start,koniec,pom):
    if n==1:
        print(f"przełóż {n} z patyka {start} na patyk {koniec}")
    else:
        wieza(n-1,start,pom,koniec)
        print(f"przełóż {n} z patyka {start} na patyk {koniec} ")
        wieza(n-1,pom,koniec,start)

wieza(5,'A','B','C')