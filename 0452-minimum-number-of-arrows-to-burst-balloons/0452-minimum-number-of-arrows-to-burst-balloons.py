class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow_height = -float('inf')
        cnt = 0
        for s, e in sorted(points, key=lambda x:x[1]):
            if not s <= arrow_height <= e:
                arrow_height = e
                cnt += 1
        return cnt