class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        if n == 0 and m == 0: return True
        if m == 0: return False
        
        dp = [[False] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
        
        for j in range(m+1):
            dp[0][j] = True
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i-1][j-1] and s[i-1] == t[j-1]:
                    dp[i][j] = True
                elif j != 1 and dp[i][j-1] and dp[i-1][j]:
                    dp[i][j] = True
        
        return dp[-1][-1]
