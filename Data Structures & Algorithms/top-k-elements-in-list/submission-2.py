class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valuecount = {}
        for i in nums:
            valuecount[i] = valuecount.get(i, 0) + 1
        ordered_list = sorted(valuecount.items(), key=lambda p:p[1], reverse=True)[:k]
        return [p[0] for p in ordered_list]