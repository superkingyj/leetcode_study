from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * (n+1)
        right = [0] * (n+1)
        result = -1
        
        left[1] = nums[0]
        right[n-1] = nums[-1]
        
        for i in range(2,n+1):
            left[i] = left[i-1] + nums[i-1]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + nums[i]
        
        for i in range(n):
            if left[i] == right[i+1]:
                result = i
                break
        
        return result

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
            
        return -1          
        