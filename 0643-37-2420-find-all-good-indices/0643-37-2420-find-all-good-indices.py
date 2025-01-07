class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        decrease = [1] * n
        increase = [1] * n
        
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                decrease[i] = decrease[i-1]+1
        
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                increase[i] = increase[i-1]+1
        
        result = []
        for i in range(k, n-k):
            if decrease[i-1] >= k and increase[i+k] >= k:
                result.append(i)
        
        return result