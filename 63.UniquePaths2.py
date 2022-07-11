from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * m for _ in range(n)]
        
        if obstacleGrid[-1][-1] == 1: return 0
        if obstacleGrid[0][0] == 1: return 0
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                up = dp[i-1][j] if obstacleGrid[i-1][j] == 0 else 0
                right = dp[i][j-1] if obstacleGrid[i][j-1] == 0  else 0
                dp[i][j] = up + right if obstacleGrid[i][j] == 0 else 0
        
        return dp[-1][-1]
    

sol = Solution()
sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])