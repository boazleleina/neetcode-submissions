class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_val = prices[0]

        for i in range(len(prices)):
            profit = prices[i] - min_val
            best_profit = max(best_profit, profit)
            min_val = min(min_val, prices[i])

        return best_profit