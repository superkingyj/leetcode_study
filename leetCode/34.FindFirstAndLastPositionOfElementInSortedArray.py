from curses.ascii import SO
from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, start, end = 0, len(nums)-1, -1, -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                if start == -1 or mid < start: 
                    start = mid
                    left = mid-1
                if mid > end: 
                    end = mid 
                    right = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return [start, end]

sol = Solution()
sol.searchRange([5,7,7,8,8,10], 8)