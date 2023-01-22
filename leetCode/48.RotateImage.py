from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # flip horizontally
        for i in range(n):
            for j in range(n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1- j] = tmp

sol = Solution()
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])