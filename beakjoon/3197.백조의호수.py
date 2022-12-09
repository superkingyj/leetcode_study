import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
cnt = 0
visited_swan = [[False] * C for _ in range(R)]
visited_water = [[False] * C for _ in range(R)]
x1, y1, x2, y2 = -1, -1, -1, -1
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
cur_water = deque()
next_water = deque()
cur_swan = deque()
next_swan = deque()

def in_range(x, y):
    return 0 <= x < R and 0 <= y < C

def init():
    global cur_swan, cur_water
    global x1, y1, x2, y2
    swan = []

    for i in range(R):
        for j in range(C):
            if grid[i][j] == "L":
                grid[i][j] = "."
                swan.append((i, j))
                visited_water[i][j] = True
                cur_water.append((i, j))
            elif grid[i][j] == ".":
                visited_water[i][j] = True
                cur_water.append((i, j))
    
    x1, y1, x2, y2 = swan[0][0], swan[0][1], swan[1][0], swan[1][1]
    visited_swan[x1][y1] = True
    cur_swan.append((x1, y1))

def bfs_swan():
    flag = False
    
    while cur_swan:
        x, y = cur_swan.popleft()

        if x == x2 and y == y2:
            flag = True
            break
            
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if in_range(new_x, new_y) and not visited_swan[new_x][new_y]:
                if grid[new_x][new_y] == ".":
                    visited_swan[new_x][new_y] = True
                    cur_swan.append((new_x, new_y))
                else:
                    visited_swan[new_x][new_y] = True
                    next_swan.append((new_x, new_y))             
    
    return flag


def bfs_water():
    while cur_water:
        x, y = cur_water.popleft()
        
        if grid[x][y] == "X": 
            grid[x][y] = "."
        
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if in_range(new_x, new_y) and not visited_water[new_x][new_y]:
                if grid[new_x][new_y] == ".":
                    visited_water[new_x][new_y] = True
                    cur_water.append((new_x, new_y))
                else:
                    visited_water[new_x][new_y] = True
                    next_water.append((new_x, new_y))

init()
while True:
    bfs_water()
    
    if bfs_swan(): 
        break

    cur_swan, cur_water = next_swan, next_water
    next_swan, next_water = deque(), deque()
    cnt += 1

print(cnt)
