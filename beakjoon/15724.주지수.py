import sys

def dp(prefix, x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

prefix = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

k = int(sys.stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp(prefix, x1, y1, x2, y2))