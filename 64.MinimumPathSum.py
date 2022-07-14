from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][1] = dp[i-1][1]+grid[i-1][0]
            
        for j in range(1, m+1):
            dp[1][j] = dp[1][j-1]+grid[0][j-1]
        
        for i in range(2, n+1):
            for j in range(2, m+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        
        return dp[-1][-1]

sol = Solution()
sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])