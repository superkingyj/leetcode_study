from typing import *

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:  
        n = len(nums)
        
        if n == 1: return nums[0]
    
        max_sum = nums[0]
        s = 0
        e = s+1
        
        for i in range(1, n):
            m = max(sum(nums[s:e]), nums[i], nums[i]+sum(nums[s:e]))

            if m == nums[i]:
                s, e = i, i+1 
                max_sum = nums[i]
            elif m == nums[i]+sum(nums[s:e]):
                e = i+1
                max_sum = m
            else:
                e = i



        # if e == n:
        #     max_sum += nums[0]
        # elif s == 1 and nums[0] > 0:
        #     max_sum += nums[0]
        
        return max_sum

sol = Solution()
# print(sol.maxSubarraySumCircular([1,-2,3,-2]))
# print(sol.maxSubarraySumCircular([5,-3,5]))
# print(sol.maxSubarraySumCircular([-3,-2,-3]))
print(sol.maxSubarraySumCircular([3,-1,2,-1]))
