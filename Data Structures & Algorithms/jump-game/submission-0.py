class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                break
            else:
                farthest = max(farthest, i + nums[i])
        
        return farthest >= len(nums)-1