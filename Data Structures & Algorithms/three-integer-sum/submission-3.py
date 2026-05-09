class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array in place
        nums.sort()
        #instantiate an empty result array
        res = []
        
        #setting element as anchor loop through the array
        for i in range(len(nums)):
            #check to ensure the anchor is not a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #check for values greater than zero, and exit early
            if nums[i] > 0:
                break
            #instantiate our pointers
            l = i+1
            r =len(nums) - 1
            #while it's a valid loop, meaning l and r haven't met
            #do the calculation
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                #if total is less than zero, we need bigger numbers
                if total < 0:
                    l += 1
                #if total is greater than zero, we need smaller numbers
                elif total > 0:
                    r -= 1
                else:
                    #if they add up to zero
                    res.append([nums[i], nums[l], nums[r]])
                    #move pointers to next step
                    l += 1
                    r -= 1
                    #if new anchor is duplicate, move pointer up
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        #return final result array
        return res
