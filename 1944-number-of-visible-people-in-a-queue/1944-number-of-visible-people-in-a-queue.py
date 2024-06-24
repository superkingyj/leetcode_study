class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        l = len(heights)
        result = [0] * l
        stack = []
        
        for i in range(l-1, -1, -1):
            while stack and stack[-1] < heights[i]:
                result[i] += 1
                stack.pop()
            
            if stack:
                result[i] += 1
            
            stack.append(heights[i])
        
        return result