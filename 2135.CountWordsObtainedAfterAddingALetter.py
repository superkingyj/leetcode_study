from typing import *
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        target_s = set()
        result = 0
        
        for word in targetWords:
            for ch in word:
                target_s.add(ch)
        
        for word in startWords:
            s = set(word)
            for i in range(97, 97+25+1):
                char = chr(i)
                if char not in s:s.add(char)
                
                diff = s - target_s
                if not diff: 
                    result += 1
                    break
                s.remove(char)
        
        return result
                    
sol = Solution()
sol.wordCount(["ab","a"], ["abc","abcd"])         
            