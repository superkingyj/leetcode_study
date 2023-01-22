from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        lpoint, rpoint = 0, len(nums) - 1
        lval = 1
        rval = 1

        while lpoint < len(nums):
            result[lpoint] *= lval 
            result[rpoint] *= rval
            lval *= nums[lpoint]
            rval *= nums[rpoint]
            lpoint += 1
            rpoint -= 1
            
        return result