import sys
from collections import deque
import copy
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chikens = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 2]
house = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1]
min_city_chiken_dist = sys.maxsize
q = deque()
dist = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
target = []

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y, new_grid):
    global visited

    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False

    return True

def push(x,y,d):
    global q
    global visited

    dist[x][y] = d
    visited[x][y] = True
    q.append((x,y))

# 집과 치킨집 사이의 최단 거리 구하기
def bfs(new_grid):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy 
            if can_go(new_x, new_y, new_grid):
                push(new_x, new_y, dist[x][y]+1)

# 치킨집 선택
def backtracking(idx, cnt):
    global min_city_chiken_dist
    global visited
    global dist
    
    if cnt == m:
        new_grid = copy.deepcopy(grid)
        city_chiken_dist = 0

        for i, j in chikens:
            if (i,j) not in target:
                new_grid[i][j] = 0
              
        for x, y in target:
            push(x,y,0)

        bfs(new_grid)

        for x, y in house:
            if visited[x][y]:
                city_chiken_dist += dist[x][y]
        
        min_city_chiken_dist = min(min_city_chiken_dist, city_chiken_dist)
        visited = [[False for _ in range(n)] for _ in range(n)]
        dist = [[0 for _ in range(n)] for _ in range(n)]
    
    if idx >= len(chikens):
        return
    
    target.append(chikens[idx])
    backtracking(idx+1, cnt+1)
    target.pop()

    backtracking(idx+1, cnt)

backtracking(0,0)
print(min_city_chiken_dist)