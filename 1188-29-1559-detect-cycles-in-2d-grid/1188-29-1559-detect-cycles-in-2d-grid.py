class Solution:
    def _in_range(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m
        
    def _can_go(self, prev_x, prev_y, new_x, new_y, grid):
        if not self._in_range(new_x, new_y): 
            return False
        if self.character != grid[new_x][new_y]: 
            return False
        if (prev_x, prev_y) == (new_x, new_y):
            return False
        return True
    
    def _dfs(self, grid, prev_x, prev_y, curr_x, curr_y) -> bool:
        if (curr_x, curr_y) in self.track:
            self.is_cycle = True
            return
        
        self.visited[curr_x][curr_y] = True
        self.track.add((curr_x, curr_y))
        
        dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
        for i in range(4):
            new_x, new_y = curr_x+dxs[i], curr_y+dys[i]
            if self._can_go(prev_x, prev_y, new_x, new_y, grid):
                self._dfs(grid, curr_x, curr_y, new_x, new_y)

        return
                
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.n, self.m = len(grid), len(grid[0])
        self.visited = [[False] * self.m for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                if not self.visited[i][j]:
                    self.start_x, self.start_y = i, j
                    self.character = grid[i][j]
                    self.track = set()
                    self.is_cycle = False
                    self._dfs(grid, -1, -1, i, j)
                    if self.is_cycle: 
                        return True
        
        return False