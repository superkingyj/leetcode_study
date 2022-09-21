import sys
import heapq
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    n, m, x = map(int, sys.stdin.readline().split())
    graph[n].append((m, x))

def dijkstra(start):
    q = [(0, start)] 
    dist = defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for m, x in graph[node]:
                alt = time + x
                heapq.heappush(q, (alt, m))
    
    return dist

result = 0
back = dijkstra(X)

for i in range(1, N+1):
    go = dijkstra(i)
    result = max(result, go[X] + back[i])

print(result)