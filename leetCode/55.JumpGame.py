from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if nums[0] == 0 and n > 1:
            return False
        
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if dp[i-1] < i: return False
            dp[i] = max(dp[i-1], i+nums[i])
        
        return True 
        
