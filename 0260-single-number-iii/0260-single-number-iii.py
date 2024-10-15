class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        visited = set()
        
        for num in nums:
            if num in visited:
                visited.remove(num)
            else:
                visited.add(num)
        
        return list(visited)