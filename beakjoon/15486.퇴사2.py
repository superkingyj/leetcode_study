import sys

N = int(sys.stdin.readline())
T = [0] * (N+1)
P = [0] * (N+1)

for i in range(1,N+1):
    t, p = map(int, sys.stdin.readline().split())
    T[i] = t
    P[i] = p

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])
    if i+T[i]-1 <= N:
        dp[i+T[i]-1] = max(dp[i-1]+P[i], dp[i+T[i]-1])

print(dp[-1])