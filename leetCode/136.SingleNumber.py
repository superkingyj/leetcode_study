class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums = [2,2,1]
        # n = 3, result = 2
        
        # nums = [4,1,2,1,2]
        # n = 5, result = 4
        n, result = len(nums), nums[0]

        
        for i in range(1,n):
            # result = 2 ^ 2 ^ 1 = 1
            # result = 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4
            result = result ^ nums[i] 

        return result