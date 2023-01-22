import sys
from pprint import pprint

N, M = map(int, sys.stdin.readline().split())
edges = list()
dist = [sys.maxsize] * (N+1)

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))

def bellman_ford(start):
    dist[start] = 0

    for i in range(N):
        for j in range(M):
            s, e, v = edges[j]
            if dist[s] != sys.maxsize and dist[e] > dist[s]+v:
                dist[e] = dist[s]+v
                if i == N-1: return True
    return False

flag = bellman_ford(1)
if flag: print(-1)
else:
    for i in range(2, N+1):
        print(-1) if dist[i] == sys.maxsize else print(dist[i])