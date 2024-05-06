class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if n <= 1:
            return nums
        
        nums.sort()
        
        result = [[num] for num in nums]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(result[i]) < len(result[j]) + 1:
                    result[i] = result[j] + [nums[i]]
        
        result.sort(key=len)
        return result.pop()
        
        