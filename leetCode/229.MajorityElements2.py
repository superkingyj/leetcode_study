from collections import defaultdict
from typing import * 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       
        #TC: O(N)
        #SC: O(N)
        
        d = defaultdict(int)
        result = []
        l = len(nums) / 3
        
        for num in nums:
            d[num] += 1
        
        for key, val in d.items():
            if val > l: result.append(key)
            
        return result