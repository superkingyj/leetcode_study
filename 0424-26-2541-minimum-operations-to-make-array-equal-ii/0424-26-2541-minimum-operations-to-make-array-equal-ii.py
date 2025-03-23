class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        n = len(nums1)
        bigger, smaller = 0, 0
        
        for i in range(n):
            if abs(nums1[i]-nums2[i]) % k != 0:
                return -1
            if nums1[i] > nums2[i]:
                bigger += (nums1[i] - nums2[i])
            else:
                smaller += (nums2[i]-nums1[i])
        
        if bigger != smaller:
            return -1
        return bigger // k
            
            