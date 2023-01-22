import sys

N, K = map(int, sys.stdin.readline().split())
arr = [0] * 1000002

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr[s+1] += 1
    arr[e+1] -= 1

for i in range(1, 1000001):
    arr[i] += arr[i-1]

left, right = 0, 0
val = 0
flag = False
while left < 1000001 and right < 1000001:
    if val == K: 
        flag = True
        break
    elif val < K:
        right += 1
        val += arr[right]
    else:
        left += 1
        val -= arr[left]

if flag: print(left, right)
else: print(0, 0)