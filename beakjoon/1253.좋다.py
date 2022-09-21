import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
result = 0

def binary_search(target, idx):
    left, right = 0, N-1

    while left < right:
        if nums[left] + nums[right] == target:
            if left == idx:
                left += 1
            elif right == idx:
                right -= 1
            else:
                return True
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    
    return False

for idx, num in enumerate(nums):
    if binary_search(num, idx):
        result += 1

print(result)