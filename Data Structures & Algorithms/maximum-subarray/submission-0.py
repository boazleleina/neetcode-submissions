class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current  = float("-inf")
        best = float("-inf")

        for i in range(len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        
        return best