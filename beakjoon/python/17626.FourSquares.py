import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    min_val = sys.maxsize
    
    j = 1
    while (j**2) <= i:
        min_val = min(min_val, dp[i-(j**2)])
        j += 1
    
    dp[i] = min_val+1

print(dp[-1])