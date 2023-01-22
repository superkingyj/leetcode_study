from typing import *

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1[0]), len(grid1)
        visited = [[False * m] for _ in range(n)]
        result = 0
        
        def in_range(x,y):
            return 0 <= x < n and 0 <= y < m
        
        def can_go(x,y):
            if not in_range(x,y): return False
            if visited[x][y] or grid1[x][y] == 0 or grid2[x][y] == 0: return False
            return True 
        
        def dfs(x,y):
            dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
            
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x+dx, y+dy
                if can_go(new_x, new_y):
                    visited[x][y] = True 
                    dfs(new_x, new_y)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid1[i][j] == 1 and grid2[i][j] == 1:
                    visited[i][j] = True
                    dfs(i,j)
                    result += 1
        
        return result


sol = Solution()
sol.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])