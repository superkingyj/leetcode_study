from collections import deque

class Solution:
    def _in_range(self, x, y):
        return 0 <= x < self.n and 0<= y < self.m

    def _can_go(self, x, y, dist):
        if not self._in_range(x, y): return False
        if self.result[x][y] <= dist: return False
        return True
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.n, self.m = len(mat), len(mat[0])
        self.result = [[0] * self.m for _ in range(self.n)]
        dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
        q = deque()
        
        for i in range(self.n):
            for j in range(self.m):
                if mat[i][j] == 0: q.append((i, j))
                else: self.result[i][j] = float(inf)
        
        while q:
            x, y = q.popleft()
            next_dist = self.result[x][y]+1
            for i in range(4):
                new_x, new_y = x+dxs[i], y+dys[i]
                if self._can_go(new_x, new_y, next_dist):
                    q.append((new_x, new_y))
                    self.result[new_x][new_y] = next_dist
        
        return self.result
                    
                    