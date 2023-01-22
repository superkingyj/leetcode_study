import sys 
import heapq
from collections import deque

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            grid[i][j] = 0
            shark_pos.append(i)
            shark_pos.append(j)
shark_size = 2
heap = []
q = deque()
visited = [[False] * n for _ in range(n)]
time = 0
eat_cnt = 0    


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y):
    if not in_range(x,y): return False
    elif visited[x][y]: return False
    elif grid[x][y] > shark_size: return False
    else: return True

def push(x,y):
    q.append((x,y))
    visited[x][y] = True

def bfs(x,y):    
    push(x,y)
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    while q:
        x, y = q.popleft()
        if 0 < grid[x][y] < shark_size: 
            heapq.heappush(heap, ((abs(shark_pos[0]-x)+ abs(shark_pos[1]-y)), x, y))
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y)

while True:
    bfs(shark_pos[0], shark_pos[1])
    if not heap:
        break

    item = heapq.heappop(heap)
    dist, x, y = item[0], item[1], item[2]
    time += dist
    eat_cnt += 1
    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1
    grid[x][y] = 0
    shark_pos[0], shark_pos[1] = x, y
    
    visited = [[False] * n for _ in range(n)]
    
print(time)
