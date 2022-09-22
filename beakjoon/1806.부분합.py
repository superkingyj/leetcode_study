import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

pre = [0] * (N+1)

for i in range(1, N+1):
    pre[i] = pre[i-1] + nums[i-1]

result, left, right = 100001, 0, 1
while left < N:
    if pre[right] - pre[left] >= S:
        result = min(result, right - left)
        left += 1
    else:
        if right < N:
            right += 1
        else:
            left += 1

print(result if result != 100001 else 0)