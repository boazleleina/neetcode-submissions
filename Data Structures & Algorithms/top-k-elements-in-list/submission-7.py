class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (val,key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [key for _, key in heap]

        return res


        

