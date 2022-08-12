from typing import *

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        #TC: O((2^n) * n^2)
        
        result = []
        
        def is_palindrome(s):
            return s == s[::-1]
        
        def backtracking(s, path):
            if not s:
                result.append(path)
                return 
            
            for i in range(1, len(s)+1):
                new_s = s[:i]
                if is_palindrome(new_s):
                     # backtracking("ab", ["a"]) -> backtracking("b", ["a", "a"]) -> backtracking("", ["a", "a", "b"]) 
                    backtracking(s[i:], path+[s[:i]])
        
        backtracking(s, [])
        return result
    
sol = Solution()
sol.partition("aab")