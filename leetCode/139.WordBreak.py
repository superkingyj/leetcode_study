from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(n+1):
            for j in range(i):
                subString = s[j:i]
                if dp[j] and subString in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]

sol = Solution()
sol.wordBreak("leetcode", ["leet", "code"])