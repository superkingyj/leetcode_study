import sys
from collections import deque

def in_range(x,y):
    return 1 <= x < N+1 and 1 <= y < N+1

def can_go(x,y, new_x, new_y):
    if not in_range(new_x, new_y): return False
    if visited[new_x][new_y]: return False
    if (new_x, new_y) in road[x][y]: return False
    else: return True 

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(x, y, new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

N, K, R = map(int, sys.stdin.readline().split())
road = [[[] for _ in range(N+1)] for _ in range(N+1)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

for _ in range(R):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1][c1].append((r2, c2))
    road[r2][c2].append((r1, c1))

cow_p = []
cow = [[False] * (N+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    cow[r][c] = True
    cow_p.append((r,c))

result = 0
for idx, item in enumerate(cow_p):
    r, c = item[0], item[1]
    visited = [[False] * (N+1) for _ in range(N+1)]
    bfs(r,c)
    for i, j in cow_p[idx+1:]:
        if not visited[i][j]: result += 1

print(result)