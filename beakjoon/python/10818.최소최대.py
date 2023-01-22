import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
max_ = -sys.maxsize
min_ = sys.maxsize

for i in range(n):
    max_ = max(max_, array[i])
    min_ = min(min_, array[i])

print(min_, max_)
