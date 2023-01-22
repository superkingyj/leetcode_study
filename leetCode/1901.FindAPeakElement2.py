from typing import *

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat)-1
        max_idx = 0
        
        while left < right:
            mid = (left + right) // 2
            max_idx = mat[mid].index(max(mat[mid]))
            
            if mat[mid][max_idx] < mat[mid+1][max_idx]:
                left = mid+1
            else: 
                right = mid
        
        max_idx = mat[mid].index(max(mat[mid]))
        return [left, max_idx]