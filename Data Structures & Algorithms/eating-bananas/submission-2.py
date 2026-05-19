class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        valid = 0

        while low <= high:
            mid = (low+high) // 2
            total = sum(math.ceil(p/mid) for p in piles)

            if total <= h:
                valid = mid
                high = mid - 1
            else:
                low = mid + 1
        return valid