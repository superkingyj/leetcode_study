import sys

N = int(sys.stdin.readline())

def check():
    global s1, s2, s3
    s1 = " " + s1
    s2 = " " + s2
    s3 = " " + s3
    N = len(s1)
    M = len(s2)
    dp = [[False] * M for _ in range(N)]
    dp[0][0] = True

    for i in range(1, N):
        if s1[i] == s3[i]: dp[i][0] = True

    for i in range(1, M):
        if s2[i] == s3[i]: dp[0][i] = True

    for i in range(1, N):
        for j in range(1, M):
            if s2[j] == s3[i+j]:
                dp[i][j] = dp[i][j-1]
            if s1[i] == s3[i+j]:
                dp[i][j] = dp[i-1][j]
            if s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
    
    return dp[-1][-1]
    
for i in range(1, N+1):
    s1, s2, s3 = sys.stdin.readline().rstrip().split()
    flag = check()
    if flag: print(f"Data set {i}: yes")
    else: print(f"Data set {i}: no")