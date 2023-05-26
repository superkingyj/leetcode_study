# DP
import sys

N = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# DP[지금까지 고려한 수의 인덱스][지금까지 고려한 박스 수의 인덱스] 
DP = [[0] * 4 for _ in range(N+1)]

for i in range(M, N+1):
    for j in range(1, 4):
        if j*M > i: DP[i][j] = DP[i][j-1]
        else: DP[i][j] = max(DP[i-M][j-1]+sum(nums[i-M+1:i+1]), DP[i][j-1], DP[i-1][j])

print(DP)
print(DP[-1][-1])