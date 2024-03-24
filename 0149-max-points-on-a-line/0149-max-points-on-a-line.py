class Solution:
    def _getGradient(self, x1, y1, x2, y2):
        if x2-x1 == 0:
            return float(inf)
        else: 
            return (y2-y1)/(x2-x1)
    
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        result = 1
        
        for i in range(len(points)):
            x1, y1 = points[i]
            gradients = defaultdict(int)
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                gradient = self._getGradient(x1, y1, x2, y2)
                gradients[gradient] += 1
                result = max(gradients[gradient], result)
        
        return result+1
                         