import sys
import bisect as bs

N, M = map(int, sys.stdin.readline().split())
level = []
title = dict()
for _ in range(N):
    t, l = sys.stdin.readline().split()
    l = int(l)
    level.append(l+1)
    if l+1 not in title: title[l+1] = t

for _ in range(M):
    input = int(sys.stdin.readline())
    l = bs.bisect_right(level, input)
    print(title[level[l]])