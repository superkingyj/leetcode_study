class Solution(object):
    def deleteAndEarn(self, nums):
        points, prev, curr = [0] * 10001, 0, 0

        for num in nums:
            points[num] += num
    
        for value in points:
            prev, curr = curr, max(prev + value, curr)
    
        return curr

sol = Solution()
print(sol.deleteAndEarn([3,4,2]))
# print(sol.deleteAndEarn([2,2,3,3,3,4]))