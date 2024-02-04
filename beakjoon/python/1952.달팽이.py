import sys

N, M = map(int, sys.stdin.readline().split())
visited = [[False] * M for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
dir = 0
x, y = 0, 0 

cnt = 0

def in_range(x,y):
    return 0 <= x <  N and 0 <= y < M

for _ in range(M*N-1):
    visited[x][y] = True
    new_x, new_y = x+dx[dir], y+dy[dir]
    
    if not in_range(new_x, new_y) or visited[new_x][new_y]:
        dir = (dir+1) % 4
        cnt += 1
        new_x, new_y = x+dx[dir], y+dy[dir]
    
    x, y = new_x, new_y

print(cnt)