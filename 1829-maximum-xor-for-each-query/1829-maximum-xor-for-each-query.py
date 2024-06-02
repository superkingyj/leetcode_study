class Solution:
    def getMaximumXor(self, nums: List[int], maximum_bit: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        result = []
        max_num = (1 << maximum_bit) -1
        
        for i in range(1, n):
            prefix.append(prefix[i-1] ^ nums[i])
        
        for i in range(n):
            result.append(prefix[i]^max_num)
        
        return result[::-1]