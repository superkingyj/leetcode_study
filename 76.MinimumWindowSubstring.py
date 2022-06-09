# import collections
# import itertools
# from typing import Collection
# from typing import List

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need = collections.Counter(t)
#         missing = len(t)
#         left = start = end = 0 

#         for right, char in enumerate(s,1):
#             missing -= need[char] > 0
#             need[char] -= 1

#             if missing == 0:
#                 while left < right and need[s[left]] < 0:
#                     need[s[left]] += 1
#                     left += 1
                
#                 if not end or right - left <= end - start:
#                     start, end, = left, right
#                     need[s[left]] += 1
#                     missing += 1
#                     left += 1
                
#         return s[start:end]

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # TC -> O(N)
        # SC -> O(M)
        
        d = dict()
        n = len(s)
        for key, val in Counter(t).items():
            d[key] = val
        
        j = -1
        min_len = 10**5
        result = ""
        # s = "BANC"
        # t = "ABC"
        # d = {"A":1, "B":1, "C":1}
        for i in range(n):
            while j+1 < n and max(d.values()) > 0:
                # j+1 = 0 -> s[j+1]="B" -> {"A":1, "B":0, "C":1}
                # j+1 = 1 -> s[j+1]="A" -> {"A":0, "B":0, "C":1}
                # j+1 = 2 -> s[j+1]="N" -> {"A":0, "B":0, "C":1}
                # j+1 = 3 -> s[j+1]="C" -> {"A":0, "B":0, "C":0}
                if s[j+1] in d: d[s[j+1]] -= 1 
                j += 1
            
            if max(d.values()) <= 0 and min_len > j-i+1:
                min_len = j-i+1
                result = s[i:j+1]
            
            if s[i] in d: d[s[i]] += 1
        
        return result

sol = Solution()
sol.minWindow("BANC", "ABC")