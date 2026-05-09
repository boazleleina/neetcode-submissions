class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # add items to set
        num_set = set(nums)

        #check if length of set is equal to length of list
        return len(num_set) != len(nums)