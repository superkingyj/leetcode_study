from typing import *
import sys

class Solution:
    def minSideJumps(self, arr: List[int]) -> int:
        n = len(arr) - 1
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = dp[0][2] = 1
        
        for i in range(1, n):
            for j in range(3):
                if arr[i] == j+1 or arr[i+1] == j+1:
                    dp[i][j] = sys.maxsize
                else:
                    dp[i][j] = min([dp[i-1][j],
                                    dp[i-1][(j+1)%3] + 1, 
                                    dp[i-1][(j+2)%3] + 1])
        return min(dp[-1])