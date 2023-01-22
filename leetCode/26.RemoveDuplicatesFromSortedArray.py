from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #TC --> O(N)
        #SC --> O(1)
        
        if len(nums) <= 1: 
            return len(nums)
        
        length = 0
        
        for i in range(1,len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
                
        return length+1