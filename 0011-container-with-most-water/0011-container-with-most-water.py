class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_result = 0
        curr = left
        
        while left <= right:
            result = min(height[left], height[right]) * (right-left)
            max_result = max(max_result, result)    
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_result
            