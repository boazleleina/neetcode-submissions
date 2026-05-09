class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            my_set.add(num)
        if len(my_set) != len(nums):
            return True
        else:
            return False
        