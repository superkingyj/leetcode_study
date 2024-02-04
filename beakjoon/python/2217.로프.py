import sys

N = int(sys.stdin.readline())
arr = list(int(sys.stdin.readline()) for _ in range(N))
arr.sort()
max_val = 0

for idx, num in enumerate(arr):
    max_val = max(max_val, num * (N-idx))

print(max_val)