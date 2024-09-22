class Solution:
    def groupThePeople(self, group_sizes: List[int]) -> List[List[int]]:
        group_sizes = [(size, idx) for idx, size in enumerate(group_sizes)]
        group_sizes.sort()
        result = []
        curr_size = 0
        curr_group = []
        
        for size, idx in group_sizes:
            curr_group.append(idx)
            curr_size += 1
            
            if curr_size >= size:
                result.append(curr_group)
                curr_size = 0
                curr_group = []
        
        return result