class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        sorted_values = sorted(count_map.items(), key=lambda p:p[1], reverse=True)[:k]
        return [p[0] for p in sorted_values]