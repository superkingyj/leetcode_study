class Solution:
    def backtracking(self, idx):
        if idx == self.n:
            for i in range(self.k):
                if self.subset[i] != self.subset_sum_val:
                    return False
            return True
        
        for i in range(self.k):
            if self.subset[i] + self.nums[idx] <= self.subset_sum_val:
                self.subset[i] += self.nums[idx]
                if self.backtracking(idx+1):
                    return True
                self.subset[i] -= self.nums[idx]
                
            if self.subset[i] == 0:
                break
        
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum_val = sum(nums)
        
        if total_sum_val % k != 0:
            return False
        
        self.nums = sorted(nums, reverse=True)
        self.k = k
        self.n = len(nums)
        self.subset_sum_val = total_sum_val // self.k
        self.subset = [0] * self.k
        
        return self.backtracking(0)
    
        