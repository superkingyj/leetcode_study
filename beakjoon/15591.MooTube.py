import sys
from collections import defaultdict, deque

N, Q = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(s, k):
    print(f"s: {s}, k:{k}")
    q = deque()
    result = []
    visited = dict()
    for key in graph.keys():
        visited[key] = False
    visited[s] = True
    q.append(s)

    while q:
        v = q.popleft()
        for v_, w in graph[v]:
            if not visited[v_] and w >= k:
                print(f"v_: {v_}")
                result.append(v_)
                visited[v_] = True
                q.append((v_))

    return len(result)

print(graph)  
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(v, k))