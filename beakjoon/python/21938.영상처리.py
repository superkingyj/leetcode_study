import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
colors = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
grid = [[0, 0, 0] * M for _ in range(N)]
visited = [[False, False, False] * M for _ in range(N)]
T = int(sys.stdin.readline())
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
cnt = 0

for i in range(N):
    for j in range(0, 3*M, 3):
        if sum(colors[i][j:j+3]) >= T*3:
            for k in range(3):
                grid[i][j+k] = 255 

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M*3

def can_go(x, y):
    if not in_range(x, y): return False
    if visited[x][y]: return False
    if grid[x][y] != 255: return False
    return True

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

for i in range(N):
    for j in range(M*3):
        if not visited[i][j] and grid[i][j] == 255:
            print(f"i, j:{i,j}")
            cnt += 1
            bfs(i, j)

print(cnt)