from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, idx = 0, len(nums)-1, -1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                left = mid+1
                idx = left
            else:
                right = mid-1
                idx = max(idx, right) if right >= 0 else 0
    
        return idx