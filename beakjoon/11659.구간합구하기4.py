import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
prefix = [0] * (N+1)

for i in range(1, N+1):
    prefix[i] = prefix[i-1]+arr[i]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(prefix[e]-prefix[s-1])