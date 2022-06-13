from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        l = len(word)
        global result
        result = False
        visited = [[False] * m for _ in range(n)]

        def in_range(x,y):
            return 0 <= x < n and 0 <= y < m
        
        def can_go(x,y,k):
            if not in_range(x,y) or k >= l: return False
            if visited[x][y]: return False
            if board[x][y] != word[k]: return False
            return True

        def dfs(x,y,k):
            global result
            dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 
            
            if k == l-1:
                result = True
                return
            
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x+dx, y+dy
                if can_go(new_x, new_y, k+1):
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y, k+1)
                    visited[new_x][new_y] = False
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    dfs(i, j, 0)
                    visited[i][j] = False
                if result: return result
        
        return result


sol = Solution()
print(sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]],"AAAAAAAAAAAAABB"))