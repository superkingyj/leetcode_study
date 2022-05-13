import re 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not re.match(p, s):
            return False
        
        match_obj = re.match(p, s)
        idxs = match_obj.span()

        if s[idxs[0]:idxs[1]] == s:
            return True
        return False
        