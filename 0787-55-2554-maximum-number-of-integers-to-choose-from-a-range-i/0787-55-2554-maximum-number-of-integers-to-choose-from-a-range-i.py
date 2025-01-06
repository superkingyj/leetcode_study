class Solution:
    def maxCount(self, banned: List[int], n: int, max_sum: int) -> int:
        banned = set(banned)
        curr_val = 0
        result = 0
        for num in range(1, n+1):
            if num not in banned and curr_val + num <= max_sum:
                result += 1
                curr_val += num
        return result
            