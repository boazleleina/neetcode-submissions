class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1

        output = []

        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output