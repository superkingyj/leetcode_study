from typing import *
import sys

# class Solution:
#     def memorization(self, nums: List[int]) -> int:
#         if not nums: return 0
#         _sum = [nums[0]]
#         for num in nums[1:]:
#             currentSum = num + _sum[-1]
#             _sum.append(max(currentSum,num))
#         print(_sum)
#         return max(_sum)

#     def kadane(self, nums: List[int]) -> int:
#         bestMax = nums[0]
#         currentSum = 0
#         for num in nums:
#             currentSum = max(num, num + currentSum)
#             bestMax = max(bestMax, currentSum)
#         return bestMax

#     def maxSubArray(self, nums: List[int]) -> int:
#         return self.kadane(nums)

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum, current_sum = -sys.maxsize, 0
        
        for num in nums:
            current_sum = max(num, current_sum+num)
            largest_sum = max(current_sum, largest_sum)
        
        return largest_sum

sol = Solution()
sol.maxSubArray()