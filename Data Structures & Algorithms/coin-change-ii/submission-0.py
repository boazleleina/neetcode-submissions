class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #create a grid, that is amount columns and different coins rows
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1
        

        for i in range(1, len(coins)+1):
            for a in range(1, amount+1):
                #current coin under consideration
                c = coins[i-1]
                #make up amount a without without coins i, or make up amoun a using coins 1 at least once so the remain amount would be amount - c
                dp[i][a] = dp[i-1][a]

                if a - c >= 0:
                    dp[i][a] += dp[i][a-c]
        
        return dp[len(coins)][amount]