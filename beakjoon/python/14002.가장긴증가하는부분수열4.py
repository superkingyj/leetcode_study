import sys

N = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)
path = [-1] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                path[i] = j

max_cnt, idx = -1, N+1
for i in range(1, N+1):
    if dp[i] > max_cnt:
        max_cnt = dp[i]
        idx = i

result = []
while idx != 0:
    result.append(arr[idx])
    idx = path[idx]

print(max_cnt)
print(*result[::-1])
