class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #create an m*n grid of 1s
        dp = [[1]* n for _ in range(m)]
        rows,cols = len(dp), len(dp[0])

        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        

        return dp[m-1][n-1]