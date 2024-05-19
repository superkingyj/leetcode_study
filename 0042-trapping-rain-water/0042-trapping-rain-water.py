class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        result = 0
        
        while left <= right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        
        return result