import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
result = []

num1 = float(sum(nums)/n)
num1 = int(round(num1, 0))
result.append(num1)

nums = sorted(nums)
num2 = nums[len(nums)//2]
result.append(num2)

min_nums = min(nums)
max_nums = max(nums)
num4 = max_nums - min_nums

count = Counter(nums)

max_count = max(count.values())
targets = [key for key, val in count.items() if val == max_count]
if len(targets) > 1:
    num3 = sorted(targets)[1]
else: num3 = targets[0]

result.append(num3)
result.append(num4)
print(*result)


