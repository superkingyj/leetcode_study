import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_cnt = 0

def get_left(idx):
    if idx == 0: return 0
    
    cnt = 0
    last_inclin = sys.maxsize
    for i in range(idx-1, -1, -1):
        inclin = (arr[idx]-arr[i]) / (idx-i)
        if inclin < last_inclin:
            cnt += 1
            last_inclin = inclin
    
    return cnt

def get_right(idx):
    if idx == N-1: return 0

    cnt = 0
    last_inclin = -sys.maxsize
    for i in range(idx+1, N):
        inclin = (arr[idx]-arr[i]) / (idx-i)
        if inclin > last_inclin:
            cnt += 1
            last_inclin = inclin
    
    return cnt

for i in range(N):
    left = get_left(i)
    right = get_right(i)
    max_cnt = max(max_cnt, left+right)

print(max_cnt)
