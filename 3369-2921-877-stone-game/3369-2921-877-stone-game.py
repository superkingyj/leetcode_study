class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for size in range(1, n):
            for i in range(n-size):
                dp[i][i+size] = max(piles[i]-dp[i-1][i+size], piles[i+size]-dp[i][i+size-1])
        
        return dp[-1][-1] > 0