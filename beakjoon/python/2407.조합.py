import sys

# nCr이라고 했을 때, nCr = n! / (n-r)!r!
# 파스칼 삼각형의 알고리즘의 점화식
# dp[n][r] = dp[n-1][r-1] + dp[n-1][r]

def dp(n, m):

    dp = [[1] * (m+1) for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(1, m+1):
            if i == j: dp[i][j] = 1
            else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[-1][-1]

n, m = map(int, sys.stdin.readline().split())
print(dp(n, m))
