class Solution:
    def _dfs(self, curr_node, trace):
        if curr_node == self.n-1:
            self.result.append(trace)
            return
        
        for next_node in self.graph[curr_node]:
            self._dfs(next_node, trace+[next_node])    
            
        
    def allPathsSourceTarget(self, _graph: List[List[int]]) -> List[List[int]]:
        self.n = len(_graph)
        self.graph = defaultdict(list)
        self.result = []
        
        for start, ends in enumerate(_graph):
            for end in ends:
                self.graph[start].append(end)
        
        self._dfs(0, [0])
        return self.result