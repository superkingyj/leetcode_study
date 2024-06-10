from collections import deque

class Solution:
    def _in_range(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m
    
    def _can_go(self, x, y):
        if not self._in_range(x,y): return False
        if self.visited[x][y]: return False
        if self.land[x][y] == 0: return False
        return True
    
    def _bfs(self, x, y):
        q = deque()
        q.append((x, y))
        self.visited[x][y] = True
        dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
        last_x, last_y = x, y
                
        while q:
            x, y = q.popleft()
            last_x, last_y = x, y
            
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x+dx, y+dy
                if self._can_go(new_x, new_y):
                    self.visited[new_x][new_y] = True
                    q.append((new_x, new_y))
        
        return last_x, last_y
    
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.n = len(land)
        self.m = len(land[0])
        self.land = land
        self.visited = [[False] * self.m for _ in range(self.n)]
        result = []
        
        for first_x in range(self.n):
            for first_y in range(self.m):
                if self._can_go(first_x, first_y):
                    last_x, last_y = self._bfs(first_x, first_y)
                    result.append([first_x, first_y, last_x, last_y])
        
        return result
        
        