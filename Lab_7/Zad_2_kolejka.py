from Zad_1_kolejka import Queue

def game(names, n):
    s = Queue()
    for i in names:
        s.enqueue(i)

    while s.size() > 1:
        for j in range(n):
            s.enqueue(s.denqueue())
        s.denqueue()

    return s.denqueue()


print(game(["Adam","Przemek","Damian","Rafał"],4))