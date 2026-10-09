class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            new_max = max(num, prev_max*num, prev_min*num)
            new_min = min(num, prev_max*num, prev_min*num)
            res = max(res, new_max)

            prev_max = new_max
            prev_min = new_min
        
        return res