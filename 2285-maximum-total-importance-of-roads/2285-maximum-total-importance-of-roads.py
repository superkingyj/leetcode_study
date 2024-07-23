class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = [0] * n
        
        for a, b in roads: 
            cnt[a] += 1
            cnt[b] += 1
        
        cnt.sort()
        return sum((idx + 1) * val for idx, val in enumerate(cnt))