from typing import *

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         idx = 0
#         for _ in range(len(nums)):
#             if nums[idx] == 0:
#                 del nums[idx]
#                 nums.append(0)
#             else:
#                 idx += 1          
        
# sol = Solution()
# sol.moveZeroes([0,0,1])

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                zero_idx += 1