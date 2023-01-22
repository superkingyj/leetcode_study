import sys

N, M = map(int, sys.stdin.readline().split())
arr = tuple(map(int, sys.stdin.readline().split()))

j, sum_val, cnt = 0, 0, 0
for i in range(N):
    while j < N and sum_val < M:
        sum_val += arr[j]
        j += 1
    
    if sum_val == M:
        cnt += 1
    
    sum_val -= arr[i]

print(cnt)