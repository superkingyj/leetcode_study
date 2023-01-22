import sys

N = int(sys.stdin.readline())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4,91):
    dp[i] = dp[i-1]*2 - dp[i-3]

print(dp[N])