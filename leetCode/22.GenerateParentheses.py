from typing import *

class Solution:
    def __init__(self):
        self.n = 0
        self.result = []
    
    def isValid(self, s):
        stack = []
        print(s)
        
        for char in s:
            print(char)
            if char == "(": 
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ")":
                    if stack.pop() == "(": 
                        continue
                    else: 
                        return False
            
        if len(stack)>0: 
            return False 
        return True
        
    
    def backtracking(self, cnt, idx):
        if cnt >= self.n:
            for i in range(len(self.array)):
                if self.array[i] == 0:
                    self.array[i] = ")"
            
            target = "".join(self.array)
            if self.isValid(target):
                self.result.append(target)
                
            return
    
        if idx >= self.n*2:
            return
        
        self.array[idx] = "("
        self.backtracking(cnt+1, idx+1)
        
        self.array[idx] = ")"
        self.backtracking(cnt, idx+1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.array = [0]* (2*n)
        self.backtracking(0, 0)
        return self.result

sol = Solution()
print(sol.generateParenthesis(3))
        