import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, N-1
result_idx = []
result_val = sys.maxsize

while left < right:
    val = arr[left]+arr[right]
    if abs(val) <= abs(result_val):
        result_val = val
        result_idx = [arr[left], arr[right]]
    if val < 0: left += 1
    else: right -= 1

print(*result_idx)