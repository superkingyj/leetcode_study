class Solution:
    def _flip_row(self, target: List[int]) -> None:
        for j in range(self.m):
            if target[j] == 0: target[j] = 1
            else: target[j] = 0
                
    def _flip_col(self, target_col: int, grid: List[List[int]]) -> None:
        for i in range(self.n):
            if grid[i][target_col] == 0: grid[i][target_col] = 1
            else: grid[i][target_col] = 0
        
    def _get_result(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(self.n):
            result += int(''.join(map(str, grid[i])), 2)
        return result
        
    def matrixScore(self, grid: List[List[int]]) -> int:
        self.n, self.m = len(grid), len(grid[0])
        
        for i in range(self.n):
            if grid[i][0] == 0:
                self._flip_row(grid[i])
        
        for j in range(1, self.m):
            zero_cnt = 0
            one_cnt = 0
            for i in range(self.n):
                if grid[i][j] == 0: zero_cnt += 1
                else: one_cnt += 1
            if zero_cnt > one_cnt:
                self._flip_col(j, grid)
        
        return self._get_result(grid)