class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Min-Heap Sort
        count = {}

        for num in nums: # --> O(n)
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for key, val in count.items(): # -> heap operation so O(log k)
            heapq.heappush(heap, (val,key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = [key for _,key in heap]

        return res

        #time complexity - > Hash map operation * min_heap operation O(n) * O (log K) = O(n*logk)
    