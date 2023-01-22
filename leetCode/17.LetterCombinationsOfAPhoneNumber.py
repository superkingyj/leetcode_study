from typing import *
from itertools import combinations

class Solution:
    # Test Case
    # "23" -> [ad, ae, af, bd, be, bf, cd, ce, cf]
    # "234" -> [adg, adh, adi .... ]
    
    # TC -> O(n*4^n)
    # SP -> O(1)
    
    def __init__(self):
        self.digit_letters = {
            "1":"",
            "2":"abc",
            "3":"def", 
            "4":"ghi", 
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"
        }

    def combinations(self, digits, register) :
        if not digits :
            return register
        
        letters = self.digit_letters[digits[0]]
        tmp_register = []

        if register:
            for item in register :
                tmp_register += [item+letter for letter in letters] 
        else:
            tmp_register += [letter for letter in letters]
            
        return self.combinations(digits[1:], tmp_register)

    def letterCombinations(self, digits: str) -> List[str]:
        return self.combinations(digits, [])