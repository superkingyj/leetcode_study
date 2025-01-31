class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        i = 0
        count = defaultdict(int)
        for j in range(len(nums)):
            k -= count[nums[j]]
            count[nums[j]] += 1
            while k <= 0:
                count[nums[i]] -= 1
                k += count[nums[i]]
                i += 1
            result += i
        return result