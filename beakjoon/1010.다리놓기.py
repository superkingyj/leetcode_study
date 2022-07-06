import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][1] = 1
    
    for j in range(1,m+1):
        dp[1][j] = j

    for i in range(2, n+1):
        for j in range(2, m+1):
            if i == j: dp[i][j] = 1
            else: dp[i][j] = dp[i-1][j-1]+dp[i][j-1]

    print(dp[-1][-1])