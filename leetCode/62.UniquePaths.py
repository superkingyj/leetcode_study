# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         dp = [[1] * m for _ in range(n)]
        
#         for i in range(n):
#             for j in range(m):
#                 dp[i] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[n-1][m-1]

# TC1 : 1, 1 -> 1
# TC2 : 2, 3 -> 3

# dp = [[1] * n for _ in range(m)]
# for(m)
#   for(n):     

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(N*M)
        # Space Complexity: O(N*M)

        # dp = [[1] * n for _ in range(m)]
        dp = [1] * n
        
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        
        return dp[-1]