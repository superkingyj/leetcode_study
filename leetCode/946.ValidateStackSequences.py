from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
         
        stack = []
        idx = 0
        
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        
        return not stack

sol = Solution()
# sol.validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
sol.validateStackSequences([1,2,3,4,5], [3,5,4,1,2])
i = 100_000_000_000