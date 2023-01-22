from typing import * 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # TC: O(NlogN)
        # SC: O(N)
        
        nums_dict = {}
        for num in nums: 
            if num in nums_dict: nums_dict[num] += 1
            else: nums_dict[num] = 1
        
        nums_list = sorted([(-val, key) for key, val in nums_dict.items()])[:k] # (a,b)
        return [key for val, key in nums_list]