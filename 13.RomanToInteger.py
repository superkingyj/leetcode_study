from operator import index


class Solution:
    
    def romanToInt(self, s: str) -> int:
        s = list(s)
        result = 0 
        minus_list = ["I", "X", "C"]
        after_list = [["V", "X"], ["L", "C"], ["D", "M"]]
        
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for idx, char in enumerate(s):
            if idx+1 < len(s) and (char in minus_list) and (s[idx+1] in after_list[minus_list.index(char)]):
                result -= roman_dict[char]
            else:
                result += roman_dict[char]
            
        return result
