class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt, prev = 0, 0
        
        for curr in flowerbed:
            if curr == 0:
                if prev == 0: cnt, prev = cnt+1, 1
                else: prev = 0
            else:
                if prev == 1: cnt -= 1
                prev = 1
        
        return cnt >= n