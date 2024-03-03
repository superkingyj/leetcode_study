from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.graph = defaultdict(deque)
        self.route = []
    
    def dfs(self, node):
        while self.graph[node]:
            next_node = self.graph[node].popleft()
            self.dfs(next_node)
        
        self.route.append(node)
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:     
        for start, end in sorted(tickets):
            self.graph[start].append(end)
        
        self.dfs("JFK")
        return self.route[::-1]
        
        
        
        
        
        
        
        
        
        
        