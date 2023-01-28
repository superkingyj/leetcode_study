# 01:32분 완료

import sys

N, K = map(int, sys.stdin.readline().split())
S = [0] + list(map(int, sys.stdin.readline().split()))
D = [0] + list(map(int, sys.stdin.readline().split()))
new_s = [0] * (N+1)

def shuffle():
    for i in range(1, N+1):
        new_s[D[i]] = S[i]

for _ in range(K):
    shuffle()
    S = new_s
    new_s = [0] * (N+1) 

print(*S[1:])

