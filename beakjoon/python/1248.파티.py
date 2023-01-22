# import sys
# import heapq
# from collections import defaultdict

# N, M, X = map(int, sys.stdin.readline().split())
# graph = defaultdict(list)

# for _ in range(M):
#     n, m, x = map(int, sys.stdin.readline().split())
#     graph[n].append((m, x))

# def dijkstra(start):
#     q = [(0, start)] 
#     dist = defaultdict(int)

#     while q:
#         time, node = heapq.heappop(q)
#         if node not in dist:
#             dist[node] = time
#             for m, x in graph[node]:
#                 alt = time + x
#                 heapq.heappush(q, (alt, m))
    
#     return dist

# result = 0
# back = dijkstra(X)

# for i in range(1, N+1):
#     go = dijkstra(i)
#     result = max(result, go[X] + back[i])

# print(result)

import sys
import heapq
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().split())
graph_back = defaultdict(list)
graph_go = defaultdict(list)

for _ in range(M):
    n, m, x = map(int, sys.stdin.readline().split())
    graph_back[n].append((m, x))
    graph_go[m].append((n, x))

def dijkstra(start, graph):
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

back = dijkstra(X, graph_back)
go = dijkstra(X, graph_go)
result = 0

for i in range(1, N+1):
    result = max(result, go[i]+back[i])
    
print(result)