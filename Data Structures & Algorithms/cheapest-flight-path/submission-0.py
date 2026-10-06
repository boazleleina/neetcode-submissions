class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #we start with the highest price possible for flights and reduce after each step
        INF = float("inf")

        #create a dist array to hold price after each 
        dist = [INF] * n

        #the first price is at source and that is 0
        dist[src] = 0

        for _ in range(k+1):
            copy = dist.copy()
            for (current_stop, next_stop, price) in flights:
                if copy[current_stop] + price < dist[next_stop]:
                    dist[next_stop] = copy[current_stop] + price
        
        if dist[dst] != INF:
            return dist[dst]
        return -1