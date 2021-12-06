'''Dany jest graf nieskierowany G = (V, E). Mówimy, że spójność
krawędziowa G wynosi k jeśli usunięcie pewnych k krawędzi powoduje, że G jest niespójny, ale usunięcie
dowolnych k − 1 krawędzi nie rozspójnia go. Proszę podać algorytm, który oblicza spójność krawędziową
danego grafu.'''

from queue import Queue
def BFS(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)

    visited[s] = True
    distance[s] = 0

    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)

    return visited[t]


def Ford_Fulkerson(G, s, t):
    n = len(G)
    parents = [None] * n
    flow = 0
    while BFS(G, s, t, parents):
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parents[current]][current] < cur_flow:
                cur_flow = G[parents[current]][current]
            current = parents[current]
        flow += cur_flow
        v = t
        while (v != s):
            G[parents[v]][v] -= cur_flow
            G[v][parents[v]] += cur_flow
            v = parents[v]
    return flow

def EdgeConnectivity(G):
    n = len(G)
    s = 0
    minflow = float('inf')
    for u in range(1, n):
        minflow = min(minflow, Ford_Fulkerson(G, s, u))
    return minflow

