from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set()
        n = len(nums)
        
        for num in nums: s.add(num)
        
        max_len = 0
        
        for i in range(n):
            num = nums[i]
            l = 0

            if num-1 not in s:
                while num in s: 
                    num += 1
                    l += 1
            
            max_len = max(max_len, l) 
        
        return max_len

sol = Solution()
sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])