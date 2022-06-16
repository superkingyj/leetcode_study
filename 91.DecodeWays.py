class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == "0": 
            return 0
        
        n = len(s)
        dp = [1] * n
        
        for i in range(1, n):
            if 0 < int(s[i]) <= 9: dp[i] = dp[i-1]
            else: dp[i] = 0
                
            if 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i-2]
            else: dp[i] += 0
                
        return dp[n-1]

sol = Solution()
print(sol.numDecodings("10"))