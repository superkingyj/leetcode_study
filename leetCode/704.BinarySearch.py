from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, target_idx = 0, len(nums)-1, -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                target_idx = mid
                break
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1  
        
        return target_idx