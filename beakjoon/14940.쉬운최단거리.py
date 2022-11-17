import sys
from pprint import pprint
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [[0]*M for _ in range(N)]
dist = [[-1]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

s_x, s_y = 0, 0
for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if inp[j] == 2: s_x, s_y = i, j
        grid[i][j] = inp[j]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

def can_go(x,y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] == 0: return False
    else: return True

def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
    q = deque()
    visited[s_x][s_y] = True
    dist[s_x][s_y] = 0
    q.append((s_x,s_y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                dist[new_x][new_y] = dist[x][y]+1
                q.append((new_x, new_y))

def print_dist():
    for i in range(N):
        for j in range(M):
            if visited[i][j]: print(dist[i][j], end = " ")
            else:
                if grid[i][j] == 0: print(0, end = " ")
                else: print(-1, end = " ")
        print()

bfs()
print_dist()