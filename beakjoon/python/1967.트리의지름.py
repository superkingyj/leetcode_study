import sys
from collections import defaultdict
from collections import deque

N = int(sys.stdin.readline())
graph = defaultdict(list)
roots = set()

for _ in range(N-1):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, w))
    roots.add(v1)

def bfs(info):
    v, w = info
    q = deque()
    visited = [False] * (N+1)
    q.append((v, w))
    diameter = 0

    while q:
        v, w = q.popleft()
        diameter = max(diameter, w)
        for _v, _w in graph[v]:
            if not visited[_v]:
                visited[_v] = True
                q.append((_v, w+_w))
    
    return diameter

print(graph)
max_diameter = 0
for v in roots:
    if len(graph[v]) < 2: 
        diameter = bfs(graph[v][0])
    else: 
        first, second = 0, 0
        for i in range(len(graph[v])):
            diameter = bfs(graph[v][i])
            if first < diameter: 
                first, second = diameter, first
            elif second < diameter:
                second = diameter
        diameter = first+second

    max_diameter = max(max_diameter, diameter)

print(max_diameter)
