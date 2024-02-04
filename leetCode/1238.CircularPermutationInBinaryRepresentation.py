class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result = [ i^(i>>1) for i in range(2 ** n)]
        idx = result.index(start)
        return result[idx:] + result[:idx]
