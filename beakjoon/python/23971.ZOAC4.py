import sys

H, W, N, M = map(int, sys.stdin.readline().split())
cnt = 0 

for i in range(1, H+1, N+1):
    for j in range(1, W+1, M+1):
        cnt += 1
        
print(cnt)
