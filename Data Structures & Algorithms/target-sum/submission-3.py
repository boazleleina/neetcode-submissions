class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0

        #total can run from -total to +total
        dp = [[0]*(2*total+1) for _ in range(len(nums)+1)]

        #to get sum 0 with 0 amounts placed is 1
        dp[0][total] = 1

        for i in range(1, len(nums)+1):
            v = nums[i-1]
            for col in range(0, (2*total)+1):
                if col+v <= 2 * total:
                    dp[i][col] += dp[i-1][col+v]
                if col - v >= 0:
                   dp[i][col] += dp[i-1][col-v]

                

        
        return dp[len(nums)][total+target]
