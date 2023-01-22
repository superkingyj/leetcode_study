from typing import *
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        
        def in_range(x,y):
            return 0 <= x < n and 0 <= y < m
        
        def can_go(x,y):
            if not in_range(x,y): return False
            elif board[x][y] == "X": return False
            elif visited[x][y]: return False
            return True
        
        def dfs(x,y):
            dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        
            board[x][y] = "#"
                     
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x+dx, y+dy
                if can_go(new_x, new_y):
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y)
       
        for j in range(m):
            if can_go(0,j): dfs(0, j)
        for i in range(n):
            if can_go(i,0): dfs(i,0)
        for j in range(m):
            if can_go(n-1,j): dfs(n-1, j)
        for i in range(n):
            if can_go(i,m-1): dfs(i, m-1)
            
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "#": board[i][j] = "O"
                elif board[i][j] == "O": board[i][j] = "X"
            

sol = Solution()
# sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# sol.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
# sol.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
# sol.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])