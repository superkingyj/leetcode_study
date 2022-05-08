class Solution:
    def twoSum(self, nums, target):
        
        ## tc1: [0, 1, 2, 0], 0 --> [0, 3]
        ## tc2: [9, 2, 3], 5 --> [1, 2]
        
        ## Time complexity -> O(N)
        ## Space complexity -> O(1)
        
        result = [] 
        
        for idx, val in enumerate(nums):
            if target-val in nums and nums.index(target-val) != idx:
                result.append(idx)
                result.append(nums.index(target-val))
                break
        
        return result


# sol = Solution()
# sol.twoSum([3,2,4], 6)

sol = Solution()
sol.twoSum([0,4,3,0], 0)