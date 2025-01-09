class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        
        for curr_start, curr_end in intervals[1:]:
            if prev_end > curr_start:
                result += 1
            else:
                prev_end = curr_end
        
        return result