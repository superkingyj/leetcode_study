class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        total_benefit = 0
        curr_price = prices[0] + fee
        
        for i in range(1, n):
            if curr_price < prices[i]:
                total_benefit += prices[i]-curr_price
                curr_price = prices[i]
            curr_price = min(prices[i]+fee, curr_price)
        
        return total_benefit