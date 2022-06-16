import sys
from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 점프를 진행하다가 현재 마지막으로 도착한 위치가 같다면
        # 지금까지의 점프 횟수가 더 적을수록 좋다
        
        nums = [0] + nums
        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0], dp[1] = 0, 0
        
        for i in range(1, n):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)
        
        return dp[n-1]
            
sol = Solution()
print(sol.jump([2,3,1,1,4]))