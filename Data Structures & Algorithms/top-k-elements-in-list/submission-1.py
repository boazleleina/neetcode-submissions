class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) + 1

        sorted_values = sorted(my_dict.items(), key=lambda p: p[1], reverse=True)
        return [p[0] for p in sorted_values[:k]]