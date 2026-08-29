class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        k = right

        while left <= right:
            hours = 0
            speed = (left + right) // 2

            for p in piles:
                hours += math.ceil(p/speed)
            
            if hours <= h:
                k = speed
                right = speed - 1
            else:
                left = speed + 1

        return k

