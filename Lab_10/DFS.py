from queue import Queue
def DFS(G):
    global time
    for u in G:
        u.p = -1
        u.visited = False

    time = 0
    for u in G:
        if not u.visited:
            DFS_Explore(u)


def DFS_Explore(u):
    global time
    time += 1
    u.time_1 = time
    u.visited = True

    for v in listE[u]:
        if v.visited == False:
            v.p = u
            DFS_Explore(v)
    time = time + 1
    u.time_2 = time
        ...

listE = {
    V[0]: [V[1], V[5]]
}
