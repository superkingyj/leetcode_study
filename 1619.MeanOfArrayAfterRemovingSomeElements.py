from statistics import mean
from typing import *

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove = int(len(arr) * 0.05)
        return mean(arr[remove:-remove])