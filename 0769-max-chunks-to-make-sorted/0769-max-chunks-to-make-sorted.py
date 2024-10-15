class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num = -1
        chunk_cnt = 0
        
        for idx, num in enumerate(arr):
            max_num = max(max_num, num)
            if max_num == idx:
                chunk_cnt += 1
        
        return chunk_cnt