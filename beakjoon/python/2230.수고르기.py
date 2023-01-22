import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(N))
arr.sort()

j, min_diff = 1, float('inf')
flag = False
for i in range(N):
    while j < N:
        diff = arr[j] - arr[i]
        if diff == M:
            flag = True
            break
        elif diff > M:
            break
        else:
            j += 1
    
    
    if diff >= M and min_diff > diff:
        min_diff = diff
        
    if flag: break
    i += 1

print(min_diff)