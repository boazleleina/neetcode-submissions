class Solution:
    def climbStairs(self, n: int) -> int:

        prev1, prev2 = 1, 1

        for _ in range(2, n+1):
            current = prev1 + prev2 # -> the current item is sum of the last two
            prev1 = prev2 # -> move up the first item by one
            prev2 = current # -> the value we just found becomes the one we use next
        
        return prev2
