from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # TC -> O(N^2)
        # SC -> O(1)
        
        if len(nums) <= 1: return nums
        
        for i in range(len(nums)-1, 0, -1): # n ~ 1
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]