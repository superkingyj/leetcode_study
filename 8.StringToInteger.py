import sys
class Solution:
    def myAtoi(self, s: str) -> int:
        
        #Test Case
        #"4932 with string" --> 4932, "   -+92" --> 0, "--1" --> 0, "" -> 0, " " -> 0
        
        #Time Complexity
        #O(N)
        #Space Complexity
        #O(N)

        s = s.lstrip()
        
        if s == "":
            return 0 

        sign = -1 if s[0] == "-" else 1
        if s[0] == "-" or s[0] == "+": s = s[1:]

        num = 0
        for char in s:
            if not str.isdigit(char):
                break
            num = num * 10 + int(char)
            
            if sign * num <= -pow(2, 31):
                return -pow(2, 31)
            if sign * num >= pow(2, 31)-1:
                return pow(2, 31)-1   
        
        return sign * num
    