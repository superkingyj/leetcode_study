import sys

N = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, N+1):
    if dp[i-1] == 0:
        dp[i] = 1
    if dp[i-3] == 0:
        dp[i] = 1
    if dp[i-4] == 0:
        dp[i] = 1

if dp[N] == 0: print("CY")
else: print("SK")