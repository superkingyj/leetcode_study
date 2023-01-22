# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right, first_bad_ver = 1, n, n
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid): 
                first_bad_ver = min(mid, first_bad_ver)
                right = mid-1
            else: 
                left = mid+1
        
        return first_bad_ver
                
                
        