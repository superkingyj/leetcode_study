import sys
from pprint import pprint

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
max_length = 0


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


# 사탕을 교환하는 함수
def switch(x1, y1, x2, y2):
    global grid
    grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]


def can_go(x, y, z):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] != z:
        return False
    return True


# 가장 긴 연속 부분(행, 열)을 찾는 함수
def dfs(x, y, z, dir_x, dir_y, l):
    global max_length

    max_length = max(max_length, l)
    visited[x][y] = True

    new_x, new_y = x + dir_x, y + dir_y
    if can_go(new_x, new_y, z):
        dfs(new_x, new_y, z, dir_x, dir_y, l + 1)


def find(s_x, s_y):
    global visited

    visited = [[False] * N for _ in range(N)]
    for x in range(s_x, N):
        for y in range(s_y, N):
            if not visited[x][y]:
                dfs(x, y, grid[x][y], dx[0], dy[0], 1)

    visited = [[False] * N for _ in range(N)]
    for x in range(s_x, N):
        for y in range(s_y, N):
            if not visited[x][y]:
                dfs(x, y, grid[x][y], dx[1], dy[1], 1)


dx, dy = [0, 1], [1, 0]  # 우, 하

for x in range(N):
    for y in range(N):
        for i in range(2):
            new_x, new_y = x + dx[i], y + dy[i]

            if not in_range(new_x, new_y):
                continue
            if grid[x][y] == grid[new_x][new_y]:
                continue

            switch(x, y, new_x, new_y)
            find(x, y)
            switch(x, y, new_x, new_y)

print(max_length)

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
