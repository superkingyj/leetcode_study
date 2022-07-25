import sys

def dp(n):

    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[-1]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp(n))
