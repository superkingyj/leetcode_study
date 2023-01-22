from typing import *

class NumMatrix:
    # TC: O(NM)
    # SC: O(NM)
    
    sum_matrix = []
    
    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                self.sum_matrix[i+1][j+1] = matrix[i][j] + self.sum_matrix[i][j+1] + self.sum_matrix[i+1][j] - self.sum_matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2+1][col2+1] - self.sum_matrix[row1][col2+1] - self.sum_matrix[row2+1][col1] + self.sum_matrix[row1][col1]
                
                
                
                
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)