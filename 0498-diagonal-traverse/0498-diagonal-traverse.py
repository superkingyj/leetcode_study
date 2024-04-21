class Solution: 
    
    def inRange(self, x, y):
        return 0 <= x < self.col and 0 <= y < self.row
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        self.row, self.col = len(mat[0]), len(mat)
        
        if self.col == 1: return mat[0]
        if self.row == 1: return [mat[r][0] for r in range(self.col)]
        dirs, curr = [(-1, 1), (1, -1)], 0 # up-right, left-down, right
        result = []
        x, y, cnt = 0, 0, 1
        
        for i in range(self.row*self.col):
            result.append(mat[x][y])
            new_x, new_y = x+dirs[curr][0], y+dirs[curr][1]
            if not self.inRange(new_x, new_y):
                new_x, new_y = (x, y+1) if curr == 0 else (x+1, y)
                if not self.inRange(new_x, new_y):
                    new_x, new_y = (x+1, y) if curr == 0 else (x, y+1)
                cnt += 1
                curr = 1-curr
            x, y = new_x, new_y
        
        return result
                
'''
(0, 0) -----------------> 0 (0)
(0, 1), (1, 0) ---------> 1 
(2, 0), (1, 1), (0, 2) -> 2
(1, 2), (2, 1) ---------> 3 
(2, 2) -----------------> 4 (m * n)

before diagonol // 2 ---> new_x, new_y = x, y+1 or x+1, y (r, d)
after diagonol // 2 ----> new_x, new_y = x+1, y or x, y+1
'''