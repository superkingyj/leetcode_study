class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        if n == 1 and m == 1:
            if matrix[0][0] == '1': return 1
            else: return 0
            
        prefix_sum = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                prefix_sum[i][j] = int(matrix[i-1][j-1]) + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        
        max_result = 0
        for x1 in range(1, n+1):
            for y1 in range(1, m+1):
                if matrix[x1-1][y1-1] == '0': continue
                if (n-x1+1) * (m-y1+1) <= max_result:continue
                for x2 in range(x1, n+1):
                    for y2 in range(y1, m+1):
                        result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1];
                        if result == (x2-x1+1) * (y2-y1+1):
                            max_result = max(max_result, result)
                        else:
                            break
        
        return max_result