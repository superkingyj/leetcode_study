class Solution:
    def _in_range(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols
    
    def _change_dir(self, dir) -> int: 
        return (dir + 1) % 4
        
    def spiralMatrixIII(self, rows: int, cols: int, curr_x: int, curr_y: int) -> List[List[int]]:
        result = [[curr_x, curr_y]]
        result_cnt = 1
        total_cnt = rows * cols
        dirs_x = [0, 1, 0, -1] 
        dirs_y = [1, 0, -1, 0] 
        dir = 0
        cnt = 0
        
        while True:
            if result_cnt >= total_cnt:
                break
            
            cnt += 1
            for _ in range(2):
                for _ in range(cnt):
                    curr_x += dirs_x[dir]
                    curr_y += dirs_y[dir]
                    if self._in_range(curr_x, curr_y, rows, cols):
                        result.append([curr_x, curr_y])
                        result_cnt += 1
                        if result_cnt >= total_cnt:
                            return result
                dir = self._change_dir(dir)
        
        return result
            