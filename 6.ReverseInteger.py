class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        result = 0
        
        while abs_x > 0:
            digit = abs_x%10
            result = result*10 + digit
            abs_x = abs_x//10

        if x < 0:
            result = -result
 
        if result > pow(2,31)-1 or result < -pow(2, 31):
            return 0 
        
        return result