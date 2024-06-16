import itertools
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.result = []
        
        for start, end in edges:
            self.graph[start].append(end)
        
        self.end_nodes = set(sum([value for value in self.graph.values()], []))
        
        for node in range(n):
            if node not in self.end_nodes:
                self.result.append(node)
                
        return self.result[0] if len(self.result) == 1 else -1