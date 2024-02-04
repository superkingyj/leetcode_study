import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [[0] * M for _ in range(N)]
target = []
dx, dy = [-1, -1, -1, 0, 1, 0, 1, 1], [-1, 0, 1, 1, 1, -1, 0, -1]

for i in range(N): 
    input = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if input[j] == 1:
            grid[i][j] = 1
            target.append((i, j))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, visited):
    if not in_range(x, y): return False
    if visited[x][y]: return False
    if grid[x][y] != 0: return False
    return True

def bfs():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    result = 0
    
    for x, y in target:
        visited[x][y] = True
        q.append((x, y, 0))
    
    while q:
        x, y, cnt = q.popleft()
        result = max(result, cnt)
        
        for i in range(8):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y, visited):
                grid[new_x][new_y] = cnt+1
                visited[new_x][new_y] = True
                q.append((new_x, new_y, cnt+1))
    
    return result

print(bfs())