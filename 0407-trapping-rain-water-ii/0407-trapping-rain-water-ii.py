import heapq

class Solution:
    def in_range(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m
    
    def is_visited(self, x, y, height_map):
        if height_map[x][y] == -1: 
            return True
        return False
    
    def can_go(self, x, y, height_map):
        if not self.in_range(x, y):
            return False
        if self.is_visited(x, y, height_map):
            return False
        return True
        
    
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        self.n, self.m = len(height_map), len(height_map[0])
        
        if self.n < 3 or self.m < 3:
            return 0
        
        hq = []
        max_height, result = 0, 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(self.n):
            for j in range(self.m):
                if i == 0 or i == self.n-1 or j == 0 or j == self.m-1:
                    heapq.heappush(hq, (height_map[i][j], i, j))
                    height_map[i][j] = -1
        
        while hq:
            height, x, y = heapq.heappop(hq)
            max_height = max(height, max_height)
            
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy
                if self.can_go(new_x, new_y, height_map):
                    heapq.heappush(hq, (height_map[new_x][new_y], new_x, new_y))
                    
                    if height_map[new_x][new_y] < max_height:
                        result += (max_height - height_map[new_x][new_y])
                    height_map[new_x][new_y] = -1
        
        return result
                    
                    
                    
            
            