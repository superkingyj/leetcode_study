import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
# 각 cctv별 한번에 체크 할 수 있는 방향 리스트
cctv_dirs = { 
    # 1의 경우 한번에 1방향 체크 가능
    # 상, 하, 좌, 우
    1: [[0], [1], [2], [3]],
    # 2의 경우 한번에 2방향 체크 가능
    # 상하, 좌우
    2: [[0,1], [2,3]],
    # 3의 경우 한번에 2방향 체크 가능
    # 상좌, 상우, 하좌, 하우
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    # 4의 경우 한번에 3방향 체크 가능
    # 상하좌, 상하우, 상좌우, 하좌우
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    # 5의 경우 한번에 4방향 체크 가능
    # 상하좌우
    5: [[0, 1, 2, 3]]
}
cctv_lst = []
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] <= 5: cctv_lst.append((i,j,grid[i][j]))

# (x,y)가 grid의 범위 안의 좌표인지 체크하는 함수
def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

# grid[x][y]가 감시 가능한 구역인지 체크하는 함수
def can_go(x,y):
    if not in_range(x,y): return False
    elif grid[x][y] == 6: return False
    else: return True

# 전달받은 _grid의 x,y 좌표로부터 dirs 방향으로 감시 가능한 구역을 체크하는 함수
def check(x,y, dirs, _grid):
    for dir in dirs:
        new_x, new_y = x, y

        while True:
            new_x, new_y = new_x+dx[dir], new_y+dy[dir]
            if can_go(new_x, new_y):
                if _grid[new_x][new_y] == 0: 
                    _grid[new_x][new_y] = "#"
            else:
                break

# 전달받은 _grid에서 체크되지 않은 영역을 카운트 하는 함수
def count_area(_grid):
    cnt = 0
    for x in range(N):
        for y in range(M):
            if _grid[x][y] == 0: cnt += 1
    return cnt

def backtracking(grid, idx):
    global result
    if idx == len(cctv_lst):
        result = min(result, count_area(grid))
        return
    
    _grid = deepcopy(grid)
    x, y, cctv = cctv_lst[idx]
    for dirs in cctv_dirs[cctv]:
        check(x, y, dirs, _grid)
        backtracking(_grid, idx+1)
        _grid = deepcopy(grid)
    
result = N*M
backtracking(grid, 0)
print(result)

