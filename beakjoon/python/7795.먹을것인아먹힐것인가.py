import sys
from bisect import bisect_left

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    
    A.sort()
    B.sort()
    
    for a in A:
        idx = bisect_left(B, a)
        cnt += idx
            
    print(cnt)