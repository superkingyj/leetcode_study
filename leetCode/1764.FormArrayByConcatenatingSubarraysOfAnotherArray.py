from typing import *

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        idx, n, flag = 0, len(nums), False
        
        for sub_group in groups:
            sub_group_len, flag = len(sub_group), False
            for i in range(idx, n):
                if i < n and nums[i:i+sub_group_len] == sub_group: 
                    idx, flag = i+sub_group_len, True
                    break
            
            if not flag: return False
            
        return True

sol = Solution()
# sol.canChoose([[1,2,3],[4,5,6]],[1,2,3,4,5,6])
# print(sol.canChoose([[10,-2],[1,2,3,4]],[1,2,3,4,10,-2]))
print(sol.canChoose([[1,2,3],[3,4]],[7,7,1,2,3,4,7,7]))