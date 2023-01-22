from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for key, val in Counter(s).items():
            if val == 1: return s.index(key)
        return -1