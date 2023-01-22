from typing import *
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jump = 1
        step = nums[0]
        reach = nums[0]
        for i in range(1,len(nums)):
            if i > step:
                jump += 1
                step = reach
            reach = max(reach, i+nums[i])

        return jump

sol = Solution()
print(sol.jump([2,3,1,1,4]))