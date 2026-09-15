class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            dist = -((point[0]**2) + (point[1]**2))
            heapq.heappush(maxHeap, (dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, point = heapq.heappop(maxHeap)
            res.append(point)
        
        return res