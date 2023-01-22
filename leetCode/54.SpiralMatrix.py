from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TC --> O(N*M)
        # SC --> O(N*M)
        
        def in_range(x,y):
            return 0 <= x < n and 0 <= y < m
        
        n = len(matrix)
        m = len(matrix[0])
        result = []
        visited = [[False]*m for _ in range(n)]
        visited[0][0] = True
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
        x, y, move_dir = 0, 0, 0
        
        for _ in range(0, n*m):
            result.append(matrix[x][y])
            visited[x][y] = True
            
            nx, ny = x+dx[move_dir], y+dy[move_dir]
            if not in_range(nx,ny) or visited[nx][ny]:
                move_dir = (move_dir+1) % 4
                x,y = x+ dx[move_dir], y+dy[move_dir]
            else:
                x,y = nx, ny
        
        return result

sol = Solution()
sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])