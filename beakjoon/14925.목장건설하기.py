import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[0] * (M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

max_val = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 0: 
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            max_val = max(max_val, dp[i][j])

print(max_val)
