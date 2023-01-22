import sys

n = int(sys.stdin.readline())

def dynamic_prog(n):
    if n == 3 or n == 3: return 1
    if n < 5: return -1
    
    dp = [sys.maxsize] * (n+1) 
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = min(dp[i-3], dp[i-5])+1
    
    return dp[-1]

result = dynamic_prog(n)
if result >= sys.maxsize: result = -1
print(result)