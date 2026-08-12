class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BRUTE FORCE
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                value = nums[i] + nums[j]
                if value == target:
                    return [i, j]
