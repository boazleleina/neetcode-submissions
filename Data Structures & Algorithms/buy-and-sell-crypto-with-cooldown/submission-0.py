class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = float("-inf")
        free = 0

        for i in range(1, len(prices)):
            #to hold today, i either was already holding yesterday, or bought today meaning you were free yesterday
            new_hold = max(hold, free - prices[i])

            #to sell today, I must have been holding yesterday
            new_sell = hold + prices[i]

            #to be free today, I was either already free yesterday or sold yesterday
            new_free = max(free, sold)

            hold = new_hold
            sold = new_sell
            free = new_free
        
        return max(sold, free)