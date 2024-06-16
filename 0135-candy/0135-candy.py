class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_cnt = [1] * n
        
        for l_idx in range(1, n):
            if ratings[l_idx-1] < ratings[l_idx]:
                candy_cnt[l_idx] = candy_cnt[l_idx-1]+1
        
        for r_idx in range(n-2, -1, -1):
            if ratings[r_idx+1] < ratings[r_idx]:
                candy_cnt[r_idx] = max(candy_cnt[r_idx], candy_cnt[r_idx+1]+1)
        
        return sum(candy_cnt)