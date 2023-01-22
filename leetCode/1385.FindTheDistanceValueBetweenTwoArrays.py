from typing import * 

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0 
        def binary_search(target):
            left, right, result = 0, len(arr2)-1, 0
            
            while left <= right:
                mid = (left + right) // 2
                
                if abs(target - arr2[mid]) <= d:
                    result += 1
                    left = mid+1
                elif abs(target - arr2[mid]) > d:
                    right = mid-1
            
            return result
        
        for num in arr1:
            if binary_search(num) <= 0:
                cnt += 1
        
        return cnt

sol = Solution()
# print(sol.findTheDistanceValue([4,5,8], [10,9,1,8], 2))
print(sol.findTheDistanceValue([4,-3,-7,0,-10], [10], 69))