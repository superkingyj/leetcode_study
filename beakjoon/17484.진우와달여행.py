import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[sys.maxsize]*3 for _ in range(M)] for _ in range(N)]

print(dp)

for y in range(M):
    for d in range(3):
        dp[0][y][d] = board[0][y]

for x in range(1, N):
    for y in range(M):
        if y == 0:
            dp[x][y][0] = min(dp[x-1][y+1][1], dp[x-1][y+1][2]) + board[x][y]
            dp[x][y][1] = dp[x-1][y][0] + board[x][y]
        elif y == M-1:
            dp[x][y][1] = dp[x-1][y][2] + board[x][y]
            dp[x][y][2] = min(dp[x-1][y-1][0], dp[x-1][y-1][1]) + board[x][y]
        else:
            dp[x][y][0] = min(dp[x-1][y+1][1], dp[x-1][y+1][2]) + board[x][y]
            dp[x][y][1] = min(dp[x-1][y][0], dp[x-1][y][2]) + board[x][y]
            dp[x][y][2] = min(dp[x-1][y-1][0], dp[x-1][y-1][1]) + board[x][y]

answer = sys.maxsize
for y in range(M):
    answer = min(min(dp[N-1][y]), answer)
print(answer)
