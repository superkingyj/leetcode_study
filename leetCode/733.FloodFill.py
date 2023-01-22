from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        visited = [[False] * m for _ in range(n)]
        def can_go(x,y,z):
            return 0 <= x < n and 0 <= y < m and not visited[x][y] and image[x][y] == z 
        
        def dfs(x, y, z):
            dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
            image[x][y] = color
            visited[x][y] = True
        
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x+dx, y+dy
                if can_go(new_x, new_y, z):
                    dfs(new_x, new_y, z)
                    
        dfs(sr, sc, image[sr][sc])
        return image

sol = Solution()
sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)