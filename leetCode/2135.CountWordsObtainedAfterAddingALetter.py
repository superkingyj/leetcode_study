from typing import *

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        startWordSet, result = set(), 0
        
        for word in startWords:
            startWordSet.add(frozenset(word))
        
        for word in targetWords:
            for i in range(len(word)):
                newWord = word[:i] + word[i+1:]
                if set(newWord) in startWordSet: 
                    result += 1
                    break
        
        return result
                    
sol = Solution()
sol.wordCount(["ab","a"], ["abc","abcd"])         
            