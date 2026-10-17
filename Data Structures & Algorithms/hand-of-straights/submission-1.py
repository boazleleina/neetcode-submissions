class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)

        minHeap = list(counts.keys())

        heapq.heapify(minHeap)

        while minHeap:

            v = heapq.heappop(minHeap)

            if counts[v] == 0:
                continue
            
            freq = counts[v]

            for i in range(v, v+groupSize):
                if counts[i] < freq:
                    return False
                counts[i] -= freq
        return True
