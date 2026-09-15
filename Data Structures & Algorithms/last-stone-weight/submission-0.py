class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y > x:
                res = y - x
                heapq.heappush(stones, -res)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0   
      