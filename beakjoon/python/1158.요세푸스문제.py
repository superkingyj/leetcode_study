import sys

n, k = map(int, sys.stdin.readline().split())
nums = [num for num in range(1, n+1)]
del_idx = k-1
answer = []

while len(nums) > 0:
    answer.append(nums[del_idx])
    del nums[del_idx]
    if len(nums) > 0: del_idx = (del_idx + k-1) % len(nums)


for i in range(n):
    if i == 0 and i == n-1: print(f"<{answer[i]}>")
    elif i == 0: print(f"<{answer[i]}, ", end = "")
    elif i == n-1: print(f"{answer[i]}>")
    else: print(f"{answer[i]}", end = ", ")