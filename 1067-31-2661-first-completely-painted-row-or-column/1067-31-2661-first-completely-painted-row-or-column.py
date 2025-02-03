class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        check_rows = [0 for _ in range(n)]
        check_cols = [0 for _ in range(m)]
        mat_dict = {mat[i][j]:(i,j) for i in range(n) for j in range(m)}
        result = 0
        
        for idx, num in enumerate(arr):
            row, col = mat_dict[num]
            check_rows[row] += 1
            check_cols[col] += 1
            if check_rows[row] == m or check_cols[col] == n:
                return idx
