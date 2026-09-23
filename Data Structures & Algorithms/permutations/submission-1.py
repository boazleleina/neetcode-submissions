class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        used = [False] * len(nums)

        curr = []

        def backtracking():
        
            if len(curr) == len(nums):
                res.append(curr.copy())
        
            for i in range(len(nums)):
                if used[i] == True:
                    continue

                curr.append(nums[i])
                used[i] = True
                backtracking()
                curr.pop()
                used[i] = False
            
        backtracking()
        return res
        

