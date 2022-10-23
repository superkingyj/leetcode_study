import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
d = defaultdict(int)
max_cnt = 0

left, right = 0, 0
while right < N:
    if d[arr[right]] < M:
        d[arr[right]] += 1
        right += 1
        max_cnt = max(max_cnt, right-left)
    else:
        d[arr[left]] -= 1
        left += 1

print(max_cnt)
