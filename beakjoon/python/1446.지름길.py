import sys
import heapq
from collections import defaultdict

N, D = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
v_set = set()

for _ in range(N):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e,c))
    v_set.add(s)
    v_set.add(e)

v_list = list(v_set)
v_list.sort()

for i in range(len(v_list)):
    if i == 0:
        graph[0].append((v_list[i], v_list[i]))
        graph[0].append((D, D))
    if D - v_list[i] >= 0:
        graph[v_list[i]].append((D, D-v_list[i]))
    if i != len(v_list)-1:
        graph[v_list[i]].append((v_list[i+1], v_list[i+1]-v_list[i]))  
    
dist = defaultdict(int)
q = []
q.append((0, 0))

while q:
    c, s = heapq.heappop(q)
    if s not in dist:
        dist[s] = c
        for e, _c in graph[s]:
            alt = c + _c
            heapq.heappush(q, (alt, e))

print(dist[D])