import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = []
        l =len(reward1)
        result = 0
        
        for idx in range(l):
            heapq.heappush(heap, (-(reward1[idx]-reward2[idx]), idx))
        
        while k:
            _, idx = heapq.heappop(heap)
            result += reward1[idx]
            k -= 1
    
        while heap:
            _, idx = heapq.heappop(heap)
            result += reward2[idx]
        
        return result