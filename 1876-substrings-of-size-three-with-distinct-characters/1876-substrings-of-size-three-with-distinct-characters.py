from collections import Counter

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = len(s)
        result = 0
        
        for idx in range(3, l+1):
            sub_string = s[idx-3:idx]
            if len(Counter(sub_string).keys()) == 3: 
                result += 1
        
        return result
        