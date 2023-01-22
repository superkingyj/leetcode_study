class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, result = 1, x, 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid ** 2 == x:
                result = mid
                break
            elif mid ** 2 > x:
                right = mid-1
                result = right
            else:
                left = mid+1
                result = left-1
                
        return result