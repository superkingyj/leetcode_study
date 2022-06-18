# import bisect

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) == 1:
#             if nums[0] == target:
#                 return 0
#             return -1
        
#         left, right = 0, len(nums)-1
        
#         while left <= right:
#             mid = left + (right - left) // 2
            
#             if nums[left] == target:
#                 return left
#             elif nums[right] == target:
#                 return right
#             elif nums[mid] == target:
#                 return mid
#             elif nums[left] < nums[mid]:
#                 if nums[left] < target and target < nums[mid]:
#                     right = mid-1
#                 else: 
#                     left = mid+1
#             else:
#                 if nums[mid] < target and target <= nums[right]:
#                     left = mid+1
#                 else:
#                     right = mid-1
                    
#         return -1

from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target: return 0
            return -1
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[left] == target: return left
            elif nums[right] == target: return right
            elif nums[mid] == target: return mid
            elif nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target < nums[right]: left = mid +1
                else: right = mid - 1
            
        return -1

sol = Solution()
sol.search([4,5,6,7,0,1,2], 3)