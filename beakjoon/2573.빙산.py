import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
ice_count = 0
visited = [[False] * M for _ in range(N)]
time = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
ice_list = []

def check_ice():
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 0: ice_list.append((i,j))
    
    return True if ice_list else False 

def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

def can_go(x,y):
    if not in_range(x,y): return False
    elif visited[x][y]: return False
    elif grid[x][y] == 0: return False
    return True

def melt_ice():
    target = set()
    while ice_list:
        i,j = ice_list.pop()
        cnt = 0
        for k in range(4):
            new_i, new_j = i+dx[k], j+dy[k]
            if in_range(new_i, new_j) and grid[new_i][new_j] == 0: cnt += 1
        target.add((i,j, grid[i][j]-cnt if grid[i][j]-cnt >= 0 else 0))
    
    for i,j,k in target:
        grid[i][j] = k

def bfs(x,y):
    visited[x][y] = True
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

while check_ice():
    ice_count = 0

    for i in range(N):
        for j in range(M):
            if can_go(i,j):
                ice_count += 1
                bfs(i,j)
    
    if ice_count >= 2: break
    visited = [[False] * M for _ in range(N)]
    melt_ice()
    
    time += 1

print(time) if ice_count > 1 else print(0)

"""
- q
- ice_count
- time
- visited
- dx, dy
- def check_ice()
    sum(grid)
- def in_range()
- def can_go()
- def melt_ice()
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(4):
                new_i, new_j = i+dx[k], j+dy[k]
                if in_range(new_i, new_j) and grid[new_i][new_j] == 0: cnt += 1
            grid[i][j] = grid[i][j] - cnt if grid[i][j] - cnt > 0 else 0
- def bfs(x,y):
    visited[x][y] = True
    q.append(x,y)
    while q:
        pass

while check_ice():
    melt_ice()
    time += 1
    for i in range(N):
        for j in range(M):
            if can_go(i,j):
                cnt += 1
                bfs()
    
    if cnt >= 2: break
    visited = False 
    cnt = 0

print(time) if cnt != 1 else print(0)
"""