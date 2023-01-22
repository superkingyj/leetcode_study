from collections import Counter

class Solution:
    def recursion(self, string, cnt, n):
        if cnt == n:
            return string
        
        new_string = ""
        count = 1
        prev = string[0]
        
        for char in string[1:]:
            if char == prev:
                count += 1
            else:
                new_string += str(count) + prev
                count = 1
                prev = char
                
        new_string += str(count) + prev
        return self.recursion(new_string, cnt+1, n)
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = self.recursion("1", 1, n)
        return result

sol = Solution()
sol.countAndSay(4)