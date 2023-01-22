from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n <= 3: return max(nums)
        
        st_nums = [0] + nums[:-1]
        dp_st = [0] * n
        dp_st[1] = st_nums[1]
        
        for i in range(2, n):
            dp_st[i] = max(dp_st[i-2]+st_nums[i], dp_st[i-1])
        
        en_nums = [0] + nums[1:]
        dp_en = [0] * n
        dp_en[1] = en_nums[1]
        
        for i in range(2, n):
            dp_en[i] = max(dp_en[i-2]+en_nums[i], dp_en[i-1])  
        
        return max(dp_st[n-1], dp_en[n-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = [0] * len(nums)
        dp1 = [0] * len(nums)
        
        if len(nums) <= 1:
            return nums[0]
        
        dp0[1] = nums[0]
        for i in range(2, len(nums)):
            dp0[i] = max(dp0[i-1], dp0[i-2]+nums[i-1])
                
        dp1[1] = nums[1]
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            
        return max(dp0[-1], dp1[-1])