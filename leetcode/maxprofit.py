class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min_left = prices[0]
        max_profit = 0
        for price_idx in range(1,len(prices)):
            max_profit = max(prices[price_idx] - min_left, max_profit)
            min_left = min(min_left, prices[price_idx])
        return max_profit
