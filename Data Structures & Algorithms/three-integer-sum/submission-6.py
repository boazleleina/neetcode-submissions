class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            #if the first value is greater than zero then no sum will equal zero
            if nums[i] > 0:
                break
            #avoid duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r]

                if target > total:
                    l+=1
                elif target < total:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l] == nums[l-1]:
                        l+=1


        return res