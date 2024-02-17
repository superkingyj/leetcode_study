class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        check = set()

        for c in s:
            if c not in check:
                check.add(c)
            else:
                result += 1
                check = set(c)
        
        return result
