from itertools import permutations
from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, len(nums)))