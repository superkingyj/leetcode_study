# class Solution:
#     def in_range_and_same(self, left, right, s):
#         return 0 <= left and right < len(s) and s[left] == s[right]
    
#     def expand(self, left, right, s):
#         while self.in_range_and_same(left, right, s):
#             left -= 1
#             right += 1
#         return s[left+1:right]
    
#     def longestPalindrome(self, s: str) -> str:  
#         # Time Complexity --> O(N^2)
#         # Space Complexity --> O(1)
        
#         if len(s) < 2 or s == s[::-1]:
#             return s
        
#         result = ""
#         for i in range(len(s)-1):
#             result = max(result, self.expand(i, i+1, s), self.expand(i, i+2, s), key=len)
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]: return s
        
        def in_range(left, right):
            return 0 <= left and right < len(s)
        
        def is_same(left, right):
            return s[left] == s[right]
        
        def expand(left, right):
            while in_range(left, right) and is_same(left, right):
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ""
        for i in range(len(s)):
            result = max(result, expand(i,i+1), expand(i, i+2), key=len)
        
        return result

sol = Solution()
sol.longestPalindrome("babad")