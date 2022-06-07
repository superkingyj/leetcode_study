from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        #TC --> O(N^2)
        #SC --> O(N)
        
        def in_range(i, j):
            return 0 <= i < n and 0 <= j < m
        
        def dfs(i, j, dx, dy):
            matrix[i][j] = 0
            new_i, new_j = i+dx, j+dy
            
            if in_range(new_i,new_j) :
                dfs(new_i, new_j, dx, dy)
        
        n = len(matrix)
        m = len(matrix[0])
        dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌
        targets = [(i,j) for i in range(n) for j in range(m) if matrix[i][j] == 0]
        
        for i, j in targets:
            for dx, dy in zip(dxs, dys):
                dfs(i, j, dx, dy)
        
        return matrix

sol = Solution()
sol.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])