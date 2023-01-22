import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    q = deque()
    visited[0][0][0] = 1
    q.append((0,0,0))
    
    while q:
        x, y, z = q.popleft()

        if x == N-1 and y == M-1: 
            return visited[x][y][z]

        for i in range(4):
            new_x, new_y = x+dxs[i], y+dys[i]
            
            if not in_range(new_x, new_y):
                continue

            if grid[new_x][new_y] == 0 and visited[new_x][new_y][z] == 0:
                visited[new_x][new_y][z] = visited[x][y][z]+1
                q.append((new_x, new_y, z))
            elif grid[new_x][new_y] == 1 and z == 0:
                visited[new_x][new_y][1] = visited[x][y][0]+1
                q.append((new_x, new_y, 1))
    
    return -1

min_dist = bfs()
print(min_dist)


"""
min_dist = sys.maxsize
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1: 
            grid[i][j] =1 
            bfs()
            if visited[-1][-1]: 
                min_dist = min(min_dist, visited[-1][-1])
            else: min_dist = -1
            grid[i][j] =1

시간복잡도
- N = 1000 / M = 10000
- BFS() -> O(V+E) = O(2000)
- 2중포문을 사용하므로 -> 10000 * 1000 * 2000 = 2000000000

"""