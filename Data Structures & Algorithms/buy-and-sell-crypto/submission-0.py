class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #instantiate max_profit to 0
        max_prof = 0
        #instantiate min_so_far as the first value in the array
        min_so_far = prices[0]
        #loop through the values in the array
        for i in range(len(prices)):
           #find max_profit_possible today
           max_prof_poss = prices[i] - min_so_far 
           #find the max of the two and apply it to max_profit
           max_prof= max(max_prof, max_prof_poss)
           #find the minimum of [i] and min_so_far and apply it to min_so_far
           min_so_far = min(min_so_far, prices[i])
        #return the max_profit
        return max_prof
