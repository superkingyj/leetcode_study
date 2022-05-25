class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #TC --> O(N)
        #SC --> O(1)
        
        l = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                return i
        
        return -1