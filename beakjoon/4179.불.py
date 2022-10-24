import sys
from pprint import pp, pprint
from collections import deque

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
f_x, f_y = 0, 0
j_x, j_y = 0, 0
visited_j = [[False] * C for _ in range(R)]
dist_j = [[0] * C for _ in range(R)]
visited_f = [[False] * C for _ in range(R)]
dist_f = [[0] * C for _ in range(R)]
exit_time = sys.maxsize
fires = []

q = deque()

def get_init_pos():
    global f_x, f_y
    global j_x, j_y
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "J":
                j_x, j_y = i, j
            elif grid[i][j] == "F":
                fires.append((i, j))

def in_range(x,y):
    return 0 <= x < R and 0 <= y < C

def can_go_j(x,y):
    if not in_range(x,y): return False
    elif visited_j[x][y]: return False
    elif visited_f[x][y]: return False
    elif grid[x][y] != ".": return False
    else: return True

def can_go_f(x,y):
    if not in_range(x,y): return False
    elif visited_f[x][y]: return False
    elif grid[x][y] == "#": return False
    else: return True

def push(x, y, type, dst):
    q.append((x,y, type))
    if type == "F": 
        visited_f[x][y] = True
        dist_f[x][y] = dst
    else: 
        visited_j[x][y] = True
        dist_j[x][y] = dst
    grid[x][y] = type

def bfs():
    global dist_f
    push(j_x, j_y, "J", 0)
    if not fires:
        dist_f = [[sys.maxsize] * C for _ in range(R)]
    else:
        for f_x, f_y in fires:
            push(f_x, f_y, "F", 0)
    
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    while q:
        x, y, type = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if type == "F":
                if can_go_f(new_x, new_y):
                    push(new_x, new_y, type, dist_f[x][y]+1)
            else:
                if can_go_j(new_x, new_y):
                    push(new_x, new_y, type, dist_j[x][y]+1)

def check_exit():
    global exit_time
    for i in range(C):
        if visited_j[0][i] and dist_j[0][i] < dist_f[0][i]:
            exit_time = min(exit_time, dist_j[0][i]+1)
    
    for i in range(R):
        if visited_j[i][0] and dist_j[i][0] < dist_f[i][0]:
            exit_time = min(exit_time, dist_j[i][0]+1)

    for i in range(C):
        if visited_j[R-1][i] and dist_j[R-1][i] < dist_f[R-1][i]:
            exit_time = min(exit_time, dist_j[R-1][i]+1)

    for i in range(R):
        if visited_j[i][C-1] and dist_j[i][C-1] < dist_f[i][C-1]:
            exit_time = min(exit_time, dist_j[i][C-1]+1)
          

get_init_pos()
bfs()
check_exit()
if exit_time == sys.maxsize: print("IMPOSSIBLE")
else: print(exit_time)
