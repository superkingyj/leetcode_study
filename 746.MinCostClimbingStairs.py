from re import S
from typing import * 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost = [0] + cost 
        n = len(cost)+1
        dp = [0 for _ in range(n)]

        
        dp[0] = 0
        dp[1] = 0
        dp[2] = 0
        
        for i in range(3, n):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        
        return dp[n-1]

sol = Solution()
sol.minCostClimbingStairs([10, 15, 20])
sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])