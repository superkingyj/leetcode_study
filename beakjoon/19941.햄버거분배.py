import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().rstrip())
cnt = 0

def in_range(x):
    return 0 <= x < N

for i in range(N):
    if arr[i] != 'P': continue

    e1, e2 = i-K, i+K
    for i in range(e1, e2+1):
        if in_range(i) and arr[i] == 'H': 
            cnt += 1
            arr[i] = "#"
            break

print(cnt)
