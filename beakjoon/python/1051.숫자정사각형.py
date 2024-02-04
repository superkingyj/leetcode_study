import sys

N, M = map(int, sys.stdin.readline().split())
grid = list(sys.stdin.readline().rstrip() for _ in range(N))
visited = [[False] * (M) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
max_width = 1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

for s_x in range(N):
    for s_y in range(M):
        for e_x in range(s_x+1, N):
            for e_y in range(s_y+1, M):
                if (e_x-s_x) != (e_y-s_y): continue
                if not (grid[s_x][s_y] == grid[e_x][s_y] == grid[s_x][e_y] == grid[e_x][e_y]): continue
                max_width = max(max_width, (e_x-s_x+1) * (e_y-s_y+1))

print(max_width)