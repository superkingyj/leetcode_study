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

