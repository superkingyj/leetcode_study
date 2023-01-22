import sys

def dp(n):
    if n == 1: return 1
    if n == 2: return 3

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007
    
    return dp[-1]


n = int(sys.stdin.readline())
print(dp(n))