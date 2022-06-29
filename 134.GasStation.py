from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
  
        n, start, left_gas = len(gas), 0, 0
        for i in range(n):
            if gas[i] + left_gas < cost[i]:
                left_gas = 0
                start = i+1
            else:
                left_gas += gas[i]-cost[i]
        
        return start