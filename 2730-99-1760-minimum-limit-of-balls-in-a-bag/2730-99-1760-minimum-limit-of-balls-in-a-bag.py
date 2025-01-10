import heapq

class Solution:
    def _can_devide(self, nums, penalty_val, max_operations):
        opr_cnt = 0
        for num in nums:
            opr_cnt += (num-1) // penalty_val
            if opr_cnt > max_operations:
                return False
        return True
        
    def minimumSize(self, nums: List[int], max_operations: int) -> int:
        left, right = 1, max(nums)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if self._can_devide(nums, mid, max_operations):
                result = mid
                right = mid-1
            else:
                left = mid+1
        
        return result
            
            
            