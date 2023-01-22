from typing import *
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        q = deque()
        global result
        global cnt
        result = 0
        cnt = 0
        
        def in_range(x,y):
            return 0 <= x < n and 0 <= y < m
        
        def can_go(x,y):
            if not in_range(x,y):
                return False
            if visited[x][y] or grid[x][y] == 0:
                return False
            return True
        
        def push(x,y):
            global cnt 
            visited[x][y] = True
            q.append((x,y))
            cnt += 1
        
        def bfs(x,y):
            dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
            global result
            global cnt
            
            while q:
                x, y = q.popleft()
                for dx, dy in zip(dxs, dys):
                    new_x, new_y = x+dx, y+dy
                    if can_go(new_x, new_y):
                        push(new_x, new_y)
            result = max(result, cnt)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    cnt = 0
                    push(i,j)
                    bfs(i,j)
        
        return result

sol = Solution()
sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])