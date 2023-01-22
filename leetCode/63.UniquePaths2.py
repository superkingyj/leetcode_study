from typing import *

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         n, m = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0] * (m+1) for _ in range(n+1)]
        
#         if obstacleGrid[-1][-1] == 1: return 0
#         if obstacleGrid[0][0] == 1: return 0
        
#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if i == 1 and j == 1: dp[i][j] = 1
#                 elif obstacleGrid[i-1][j-1] == 0: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (m+1)
        
        if obstacleGrid[-1][-1] == 1: return 0
        if obstacleGrid[0][0] == 1: return 0
        
        dp[1] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if obstacleGrid[i-1][j-1] == 1: dp[j] = 0
                elif j > 1: dp[j] += dp[j-1]
                
        return dp[-1]

sol = Solution()
sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])