# class Solution:
#     def numDecodings(self, s: str) -> int:
        
#         if not s or s[0] == "0": 
#             return 0
        
#         n = len(s)
#         dp = [1] * n
        
#         for i in range(1, n):
#             if 0 < int(s[i]) <= 9: dp[i] = dp[i-1]
#             else: dp[i] = 0
                
#             if 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i-1]
#             else: dp[i] += 0
                
#         return dp[n-1]

# sol = Solution()
# print(sol.numDecodings("10"))

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0": return 0
        
        n = len(s)
        dp = [1] * (n+1)
        dp[1] = 1
        
        for i in range(2, n+1):
            if 1 <= int(s[i-1]) <= 9: dp[i] = dp[i-1]
            else: dp[i] = 0
            
            print(s[i-2:i])
            if 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i-2]
        
        return dp[-1]
    

sol = Solution()
print(sol.numDecodings("10"))
