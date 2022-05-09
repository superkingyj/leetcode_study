import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
nums = [i for i in range(1,n+1)]
nums = deque(nums)
cnt = 0
josephus = []

while True:
    if not nums:
        break
    
    if cnt == k-1:
        josephus.append(nums[0])
        del nums[0]
        cnt = 0
    else:
        nums.append(nums[0])
        del nums[0]
        cnt += 1

print("<", end="")
[print(josephus[i], end =", ") for i in range(len(josephus)) if i != len(josephus)-1]
print(josephus[len(josephus)-1], end=">")

