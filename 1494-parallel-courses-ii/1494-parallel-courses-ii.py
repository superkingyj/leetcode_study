from collections import defaultdict
import heapq

class Solution:
    def can_go(self, next_class, taken_classes):
        if next_class in taken_classes:
            return False
        return all(v in taken_classes for v in self.graph[next_class])
    
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.graph = defaultdict(list)
        
        for _from, _to in relations:
            self.graph[_to].append(_from)
        
        start_classes = {v for v in range(1, n+1) if v not in self.graph}
        
        heap = [(1, frozenset(x)) for x in combinations(start_classes, min(k, len(start_classes)))]
        heapq.heapify(heap)
        visited = set()
        result = -1
        
        while heap:
            curr_semester, taken_classes = heapq.heappop(heap)
            
            if len(taken_classes) == n:
                result = curr_semester
                break
            
            next_classes = [next_class for next_class in range(1, n+1) if self.can_go(next_class, taken_classes)]
            
            for next_class in combinations(next_classes, min(k, len(next_classes))):
                new_taken_classes = frozenset(taken_classes.union(next_class))
                if (new_taken_classes, curr_semester+1) not in visited:
                    heapq.heappush(heap, (curr_semester+1, new_taken_classes))
                    visited.add((new_taken_classes, curr_semester+1))
        
        return result
                    
        
        