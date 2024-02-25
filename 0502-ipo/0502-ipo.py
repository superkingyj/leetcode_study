import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        cap_n_prof = [(capital[i], profits[i]) for i in range(n)]
        cap_n_prof.sort()
        
        pq, idx = [], 0
        for _ in range(k):
            while idx < n and cap_n_prof[idx][0] <= w:
                cap, prof = cap_n_prof[idx]
                heapq.heappush(pq, -prof)
                idx += 1
            
            if pq: w -= heapq.heappop(pq)
            else: break
        
        return w