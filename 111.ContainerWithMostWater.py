from typing import List
import sys

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Time Complexity --> O(1)
        #Space Complexity --> O(1)
        
        water = -sys.maxsize
        left, right = 0, len(height)-1
        
        while left < right:
            
            new_water = (right - left) * min(height[left], height[right])
            water = max(water, new_water)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1 
                
        return water