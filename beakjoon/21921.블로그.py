import sys

N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix = [0] * N
max_num = 0
cnt = 0

for i in range(N):
    prefix[i] = prefix[i-1] + arr[i]

for i in range(X-1, N):
    num = prefix[i]-(prefix[i-X] if i-X >= 0 else 0) 
    max_num = max(max_num, num)

for i in range(X-1, N):
    num = prefix[i]-(prefix[i-X] if i-X >= 0 else 0) 
    if num == max_num:
        cnt += 1

if max_num == 0:
    print("SAD")
else: 
    print(max_num)
    print(cnt)