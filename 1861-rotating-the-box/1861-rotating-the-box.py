class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        new_box = [["."] * n for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
                new_box[j][n-i-1] = box[i][j]
    
    
        new_n, new_m = m, n
        
        for j in range(new_m):
            new_x, new_y = new_n-1, j
            for i in range(new_n-1, -1, -1):
                if new_box[i][j] == "#": 
                    new_box[i][j] = "."
                    new_box[new_x][new_y] = "#"
                    new_x = new_x-1
                elif new_box[i][j] == "*": new_x = i-1
                elif new_box[i][j] == ".": new_x = max(new_x, i)
        
        return new_box