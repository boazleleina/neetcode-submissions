class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")

        dist = [INF] * n

        dist[src] = 0


        for _ in range(k+1):
            copy = dist.copy()

            for (current_stop, next_stop, price) in flights:
                if copy[current_stop] + price < dist[next_stop]:
                    dist[next_stop] = copy[current_stop] + price
        
        if dist[dst] != INF:
            return dist[dst]
        return -1