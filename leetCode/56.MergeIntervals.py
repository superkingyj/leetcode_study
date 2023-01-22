from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # TC --> O(NlogN)
        # SC --> O(N)
        
        points = []
        
        for interval in intervals:
            x1,x2 = interval[0], interval[1]
            points.append((x1, -1, 1))
            points.append((x2, 0, -1))
        
        points.sort()
        result = []
        sum_val, start_x, end_x = 0, -1, -1
        
        for idx, item in enumerate(points):
            x, v = item[0], item[2]
            sum_val += v
        
            if sum_val >= 2 and start_x < 0: # 구간 시작
                start_x = points[idx-1][0]
            elif sum_val == 0 and start_x > 0: # 구간 끝
                end_x = x
                result.append([start_x, end_x])
                start_x, end_x = -1, -1
            elif sum_val == 1 and v == 1:
                start_x = x
            elif sum_val == 0 and v == -1:
                end_x = x
                result.append([start_x, end_x])
                start_x, end_x = -1, -1
                
        return result
            
sol = Solution()  
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
            
        