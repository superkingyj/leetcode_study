class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = "0"
        
        for _ in range(n):
            new_result = result + "1" + "".join([str(1-int(char)) for char in result[::-1]])
            result = new_result
        
        return result[k-1]
            