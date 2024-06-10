class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        cnt = 0
        start, end = -1, 0 
        for _start, _end in clips:
            if end >= time or _start > end:
                break
            if start < _start <= end:
                cnt += 1
                start = end
            end = max(end, _end)
        
        return cnt if end >= time else -1
        
        
            