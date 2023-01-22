from typing import *

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr, ans = 0, 0
        even, odd = 1, 0
        mod = 10**9 +7
        
        for i in arr :
            curr += i 
            print(f"curr:{curr}, ans:{ans}, even:{even}, odd:{odd}")
            if curr%2 == 1 :
                odd += 1
                ans = (ans+even)%mod
            else:
                even += 1
                ans = (ans+odd)%mod
        return ans%mod

sol = Solution()
sol.numOfSubarrays([1,3,5])