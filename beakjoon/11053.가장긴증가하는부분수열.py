import sys

def dp(N, arr):
    dp = [1] * N
    
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]: dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

N = int(sys.stdin.readline())
arr = [int(i) for i in sys.stdin.readline().split()]
print(dp(N, arr))
