import sys
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = True

    for _v in graph[v]:
        if not visited[_v]:
            dfs(_v)

dfs(1)
print(visited.count(True)-1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""