class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1, len(coins)+1):
            for a in range(1, amount+1):
                #the current coin we are considering
                c = coins[i-1]

                #to reach amount, check without coins i
                dp[i][a] = dp[i-1][a]

                #also consider reaching the amount with at least one of the coins
                if a-c >= 0:
                    dp[i][a] += dp[i][a-c]

        return dp[len(coins)][amount]