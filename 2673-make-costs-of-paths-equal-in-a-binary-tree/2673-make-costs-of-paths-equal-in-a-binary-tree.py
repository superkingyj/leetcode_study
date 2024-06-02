class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost = [0] + cost
        result = 0
        
        for i in range(n//2, 0, -1):
            left_cost, right_cost = cost[2*i], cost[2*i+1]
            if left_cost > right_cost:
                result += (left_cost - right_cost)
                cost[i] += left_cost
            else:
                result += right_cost - left_cost
                cost[i] += right_cost
        
        return result