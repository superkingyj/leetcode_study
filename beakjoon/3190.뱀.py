import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples_info = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
l_info = [list(sys.stdin.readline().split()) for _ in range(l)]
times = deque([int(item[0]) for item in l_info])
dirs = deque([item[1] for item in l_info])
grid = [[0] * (n+2) for _ in range(n+2)]
time = 0 

def init_grid():
    global grid, apples_info

    for i in range(n+2):
        for j in range(n+2):

            if i == 0 or j == 0 or i == n+1 or j == n+1:
                grid[i][j] = 1 # 벽: 1
            
            if (i, j) in apples_info:
                grid[i][j] = 2 # 사과: 2

def move(x, y):
    global grid, times, dirs, time
    snake, d = deque(), 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
    flag = False
    snake.append((x, y))
    
    while True:

        if flag:
            break

        if len(times) and time == times[0]:
            if dirs[0] == "D":
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4
                
            times.popleft()
            dirs.popleft()

        new_x, new_y = x + dxs[d], y + dys[d]

        # 벽 또는 자기 자신이면 종료
        if grid[new_x][new_y] == 1 or (new_x, new_y) in snake:
            flag = True
        # 사과면
        elif grid[new_x][new_y] == 2:
            grid[new_x][new_y] = 0
            snake.appendleft((new_x, new_y))
        else:
            snake.pop()
            snake.appendleft((new_x, new_y))

        x, y = new_x, new_y
        time += 1

init_grid()     
move(1, 1)
print(time)
        


