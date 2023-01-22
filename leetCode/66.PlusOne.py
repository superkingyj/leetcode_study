from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_s = "".join(map(str, digits))
        num_i = int(num_s)
        return list(str(num_i+1))