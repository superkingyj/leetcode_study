import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [0] * (N+1)
result = 0

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[e].append(s)
 
X = int(sys.stdin.readline())

def dfs(v):
    global result
    visited[v] = True
    for _v in graph[v]:
        if not visited[_v]:
            result += 1
            dfs(_v)

dfs(X)
print(result)