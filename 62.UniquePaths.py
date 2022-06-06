class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                dp[i] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]