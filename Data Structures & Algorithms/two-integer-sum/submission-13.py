class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffNums = {}

        for i in range(len(nums)):
            value = target - nums[i]

            if value in diffNums:
                return [diffNums[value], i]
            diffNums[nums[i]] = i
