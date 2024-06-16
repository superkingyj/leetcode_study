from collections import defaultdict
class Solution:
    def _dfs(self, v, visited):
        self.cnt += 1
        visited[v] = True
        
        for next_v in self.graph[v]:
            if not visited[next_v]:
                self._dfs(next_v, visited)

    def _inside_a_circle(self, x1, y1, r1, x2, y2):
        if (x1-x2)**2 + (y1-y2)**2 <= r1*r1: 
            return True
        return False
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        l = len(bombs)
        self.graph = defaultdict(list)
        result = 0
        
        for i in range(l):
            x1, y1, r1 = bombs[i]
            for j in range(l):
                if i == j: continue
                x2, y2, r2 = bombs[j]
                if self._inside_a_circle(x1, y1, r1, x2, y2):
                    self.graph[i].append(j)
        
        for i in range(l):
            self.cnt = 0
            self._dfs(i, [False] * l)
            result = max(result, self.cnt)
        
        return result
            