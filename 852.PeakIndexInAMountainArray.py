from typing import *

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr = [-1] + arr + [-1]
        left, right, result = 1, len(arr)-2, -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                result = mid-1
                break
            elif arr[mid-1] > arr[mid]:
                right = mid-1
            else:
                left = mid+1
        
        return result
        
sol = Solution()
sol.peakIndexInMountainArray([3,9,8,6,4])