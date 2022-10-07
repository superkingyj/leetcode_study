import sys

R, C = map(int, sys.stdin.readline().split())
grid = list(sys.stdin.readline() for _ in range(R))
alphabets = [False] * 26
cnt = 0
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x,y):
    return 0 <= x < R and 0 <= y < C

def can_go(x,y):
    if not in_range(x,y): return False
    elif alphabets[ord(grid[x][y])%26]: return False
    else: return True

def dfs(x,y,z):
    global cnt
    cnt = max(cnt, z)
    alphabets[ord(grid[x][y])%26] = True

    for i in range(4):
        new_x, new_y = x+dxs[i], y+dys[i]
        if can_go(new_x, new_y):
            dfs(new_x, new_y, z+1)

    alphabets[ord(grid[x][y])%26] = False

dfs(0,0,1)
print(cnt)