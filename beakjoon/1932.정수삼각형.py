import sys

N = int(sys.stdin.readline())
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    input = list(map(int, sys.stdin.readline().split()))
    for j in range(1, i+1):
        dp[i][j] = input[j-1]

for i in range(N+1):
    for j in range(1, i+1):
        dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))