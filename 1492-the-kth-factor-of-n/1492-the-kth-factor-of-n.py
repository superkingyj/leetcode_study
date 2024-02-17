class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nums = set()

        for i in range(1, int(n ** (1/2))+1):
            if n % i == 0: 
                nums.add(i)
                nums.add(n//i)
        
        if len(nums) < k: return -1
        return sorted(nums)[k-1]