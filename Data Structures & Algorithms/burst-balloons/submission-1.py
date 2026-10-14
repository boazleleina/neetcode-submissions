class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        arr = [1] + nums + [1]

        dp = [[0] * (n+2) for _ in range(n+2)]

        # 3. Outer loop: length of the interval (gap between left and right walls)
        # We need at least 1 balloon between walls, so the minimum gap is 2.
        # The maximum gap covers the entire padded array: n + 1
        for length in range(2, n+2):

            # 4. Middle loop: sliding the left wall
            # The left wall can go up to (n + 1) - length before the right wall goes out of bounds
            for left in range(n+2-length):
                right = left + length

                for k in range(left+1, right):
                    # Compute the coins gained by bursting k last in this interval
                    current_coins = arr[left] * arr[k] * arr[right]

                    # Total is the current coins + the max coins from the left and right subproblems
                    total = current_coins + dp[left][k] + dp[k][right]

                    # Update the DP table with the best outcome for this interval
                    dp[left][right] = max(dp[left][right], total)
        
        return dp[0][n+1]
