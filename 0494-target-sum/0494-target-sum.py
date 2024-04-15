class Solution:
    def _backtracking(self, idx, val) -> int:
        if idx == self.l:
            return 1 if val == self.target else 0
        
        if (idx, val) in self.dp:
            return self.dp[(idx, val)]
        
        self.dp[(idx, val)] = self._backtracking(idx+1, val+self.nums[idx]) + self._backtracking(idx+1, val-self.nums[idx])
        
        return self.dp[(idx, val)]
                
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.l = len(nums)
        self.target = target
        self.dp = {}
        return self._backtracking(0, 0)
        
        