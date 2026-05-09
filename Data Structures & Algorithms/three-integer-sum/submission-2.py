class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the order of nums
        nums.sort()
        #initiate result list
        res = []
        #start at the beginning of the list and set and anchor
        for i in range(len(nums)):
            #if the value of nums[i] is non-negative then no triplet
            if nums[i] > 0:
                break
            #avoid duplicate anchor:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #instantiate the two pointers
            l = i+1
            r = len(nums) - 1
            while l < r:
                #find the total of the triplets
                total = nums[i] + nums[l] + nums[r]
                #if it's too small, then we need bigger numbers
                if total < 0:
                    l+=1
                #if it's too big, we need smaller numbers
                elif total > 0:
                    r-=1
                #if it's right, append it to results
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    #skip duplicates of l
                    while l<r and nums[l] == nums[l-1]:
                        l+=1

            
        return res
