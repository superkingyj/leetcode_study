class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def can_go(x,y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0
        
        grid = [[0] * n for _ in range(n)]
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
        dir, x, y, num = 0, 0, 0, 1

        for i in range(n*n):
            grid[x][y] = num
            
            new_x, new_y = x + dx[dir], y+dy[dir]
            
            if not can_go(new_x, new_y):
                dir = (dir + 1) % 4
                new_x, new_y = x + dx[dir], y+dy[dir]
            
            x, y = new_x, new_y
            num += 1
        
        return grid