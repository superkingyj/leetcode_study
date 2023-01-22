from typing import *
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            if x+y > y+x: return 1
            elif x+y == y+x:return 0
            else: return -1
        
        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(compare), reverse = True)
        return "".join(nums).lstrip("0") or "0"