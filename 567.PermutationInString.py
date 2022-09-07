from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d, idx, check, result = defaultdict(int), 0, defaultdict(int), False
        for char in s1:
            s1_d[char] += 1
            check[char] += 1
        
        for i in range(len(s2)):
            while idx < len(s2) and s2[idx] in check and check[s2[idx]] > 0:
                check[s2[idx]] -= 1
                idx += 1
                result = True if sum(check.values()) == 0 or result else False
                    
            if s2[i] in s1_d:
                check[s2[i]] += 1
            else:
                idx += 1
                            
        return result