import sys

N = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp[1:]))