import sys
import heapq
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(8):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

dist = defaultdict(int)
q = []
q.append((0, 1))

while q:
    c, s = heapq.heappop(q)
    if s not in dist:
        dist[s] = c
        for e, _c in graph[s]:
            alt = c + _c
            heapq.heappush(q, (alt, e))

print(dist)
print(dist[N])