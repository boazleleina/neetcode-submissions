class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_hash:
                return [my_hash[complement], i]
            my_hash[nums[i]] = i
        