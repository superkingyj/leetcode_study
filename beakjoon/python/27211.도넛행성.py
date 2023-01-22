import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
visited = [[False] * M for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
cnt = 0

def can_go(x, y):
    if visited[x][y]: return False
    if grid[x][y] == 1: return False
    return True

# 도넛형태의 좌표를 구하는 함수
def get_pos(x, y):
    new_x, new_y = x, y
    
    if x < 0: new_x = N-1
    elif x >= N: new_x = 0
    
    if y < 0: new_y = M-1
    elif y >= M: new_y = 0
    
    return new_x, new_y

def bfs(x, y):
    global cnt
    
    cnt += 1
    q = deque()
    visited[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x, new_y = get_pos(x+dx[i], y+dy[i])

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

print(cnt)