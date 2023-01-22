import sys

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N
        
# 사탕을 교환하는 함수
def switch(x1, y1, x2, y2):
    global grid
    grid[x1][y1], grid[x2][y2] =  grid[x2][y2], grid[x1][y1]

# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분 행을 구하는 함수
def get_max_c(x, y):
    max_cnt = 0

    # grid[x][y] 기준 왼쪽 탐색
    left = y
    while True:
        if left >= 0 and grid[x][y] == grid[x][left]:
            left -= 1
        else: break
    max_cnt = max(max_cnt, y-left+1 if left >= 0 else y+1)
    
    # grid[x][y] 기준 오른쪽 탐색
    right = y
    while True:
        if right < N and grid[x][y] == grid[x][right]:
            right += 1
        else: break
    max_cnt = max(max_cnt, right-y if right < N else N-y)

    return max_cnt

# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분 열을 구하는 함수
def get_max_r(x, y):
    max_cnt = 0

    # grid[x][y] 기준 위쪽 탐색
    up = x
    while True:
        if up >= 0 and grid[x][y] == grid[up][y]:
            up -= 1
        else: break
    max_cnt = max(max_cnt, x-up+1 if up >= 0 else x-0)
    
    # grdi[x][y] 기준 아래쪽 탐색
    down = x
    while True:
        if down < N and grid[x][y] == grid[down][y]: 
            down += 1
        else: break
    max_cnt = max(max_cnt, down-x if down < N else N-x)

    return max_cnt

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, get_max_r(i,j), get_max_c(i,j))

print(result)

dx, dy = [0, 1], [1, 0] # 우,하
target = set()
for i in range(N):
    for j in range(N):
        if in_range(i, j+1) and grid[i][j] != grid[i][j+1]:
            switch(i, j, i, j+1)
            result = max(result, get_max_r(i, j), get_max_c(i, j))
            if in_range(i+1, j+1):
                result = max(result, get_max_r(i+1, j+1), get_max_c(i+1, j+1))
            switch(i, j, i, j+1)
        if in_range(i+1, j) and grid[i][j] != grid[i+1][j]:
            switch(i, j, i+1, j)
            result = max(result, get_max_r(i, j), get_max_c(i, j))
            if in_range(i+1, j+1):
                result = max(result, get_max_r(i+1, j+1), get_max_c(i+1, j+1))
            switch(i, j, i+1, j)
        if result== 4: print(i,j)

print(result)


















"""
CCP
CCP
PPC

1)2개
CPC
CCP
PPC

2)2개
CCP
CPC
PPC

3)3개
CCP
CCP
PCP

_____________
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

1) 
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
"""