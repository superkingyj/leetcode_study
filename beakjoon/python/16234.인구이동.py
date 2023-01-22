import sys
from collections import deque 
from pprint import pprint

N, L, R = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque()
target = []
people_num = 0
date = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

def can_go(x,y,z):
    if not in_range(x,y): return False
    elif visited[x][y]: return False
    elif abs(grid[x][y] - z) > R: return False
    elif abs(grid[x][y] - z) < L: return False
    else: return True

def push(x,y):
    visited[x][y] = True
    q.append((x,y))

def bfs(x,y):
    global people_num
    push(x,y)

    while q:
        x, y = q.popleft()
        people_num += grid[x][y]
        target.append((x,y))
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y, grid[x][y]):
                push(new_x, new_y)
    
def move_people():
    global people_num
    if not target: return
    if not people_num: return
    people_num = people_num // len(target)
    
    while target:
        x, y = target.pop()
        grid[x][y] = people_num
        
    people_num = 0

while True:
    flag = False
    for i in range(N):
        for j in range(N):
            for k in range(4):
                new_i, new_j = i+dx[k], j+dy[k]
                if in_range(new_i, new_j) \
                and L <= abs(grid[new_i][new_j] - grid[i][j]) <= R \
                and not visited[i][j]:
                    flag = True
                    bfs(i, j)    
                    move_people()

    if not flag: break
    date += 1 
    visited = visited = [[False] * N for _ in range(N)]

print(date)