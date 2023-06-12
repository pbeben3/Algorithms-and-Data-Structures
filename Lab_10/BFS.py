from queue import Queue

def BFS(G,s):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    p = [-1] * n

    visited[s] = True
    d[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                p[v] = u
                Q.put(v)

    return visited, d, p

#graf
G = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
]

startV = 3


visited, distance, parent = BFS(G,startV)
for v in range(len(G)):
    print(f'Wierzchołek {v}: visited = {visited[v]}, distance = {[v]}, paren = {parent[v]}')