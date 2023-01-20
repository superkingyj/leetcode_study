import sys
from pprint import pprint

N = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    for j in range(len(input)):
        arr[i][j] = input[j]
dp = [[0] * (N) for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(N-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i][j]+arr[i+1][j], dp[i+1][j])
        dp[i+1][j+1] = max(dp[i][j]+arr[i+1][j+1], dp[i+1][j+1])

pprint(dp)
print(max(dp[-1]))