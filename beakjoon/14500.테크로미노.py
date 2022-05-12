import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_sum = 0
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 동, 남, 서, 북
visited = [[False]*m for _ in range(n)]
exec_pos_list = list(combinations(range(4), 3))

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def dfs(x, y, cnt, sum_):
    global max_sum, dxs, dys

    if cnt == 4:
        max_sum = max(max_sum, sum_)
        return
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, cnt+1, sum_+grid[new_x][new_y])
            visited[new_x][new_y] = False

def exce(x, y):
    global exec_pos_list, max_sum

    for exec_post in exec_pos_list:
        sum = grid[x][y]

        for num in exec_post:
            new_x = x + dxs[num]
            new_y = y + dys[num]
            if not can_go(new_x, new_y):
                sum = 0
                break    
            sum += grid[new_x][new_y]
            
        max_sum = max(max_sum, sum)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = False
    
        exce(i, j)

print(max_sum)