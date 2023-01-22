import sys
from xml.dom import INDEX_SIZE_ERR

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        substring = dict()
        start = 0
        max_len = -sys.maxsize
        
        for idx, char in enumerate(s):
            if char not in substring:
                substring[char] = idx
            else:
                start = substring[char] + 1
                substring[char] = idx
            max_len = max(max_len, idx - start+1)
        
        return max_len
                
            

sol = Solution()
# print(sol.lengthOfLongestSubstring("dvdf"))
# print(sol.lengthOfLongestSubstring("abcabcbb"))
# print(sol.lengthOfLongestSubstring("bbbbb"))
# print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abba"))