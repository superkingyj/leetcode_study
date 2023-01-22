from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 풀이1
        # TC
        # [0, -1, 2], [1, 3] --> [-1, 0, 1, 2, 3] --> 1
        # Time Complexity -> O(NlogN)
        # Space Complexity -> O(N)
        
        nums = sorted(nums1+nums2)
        
        if len(nums) % 2:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2]+nums[len(nums)//2-1]) / 2