from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        points = []
        
        for interval in intervals:
            x1 = interval[0]
            x2 = interval[1]
            
            points.append((x1, -1, 1))
            points.append((x2, 0, -1))
        
        points.sort()
        result = []
        sum_val, start_x, end_x = 0, -1, -1
        
        for idx, item in enumerate(points):
            x, v = item[0], item[2]
            sum_val += v
        
            if sum_val >= 2 and start_x < 0:
                start_x = points[idx-1][0]
            
            if sum_val == 0 and start_x > 0:
                end_x = x
                result.append([start_x, end_x])
                start_x, end_x = -1, -1
        
        return result
            
sol = Solution()  
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
            
        