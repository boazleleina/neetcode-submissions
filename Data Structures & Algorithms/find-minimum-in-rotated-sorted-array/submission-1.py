class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initiate low, high
        low, high = 0, len(nums)-1
        #loop while low is less than high:
        while low < high:
            #calculate mid
            mid = (low + high) // 2
            #if the mid is greater than nums[-1]:
            if nums[mid] > nums[-1]:
                #low moves to mid+1
                low = mid + 1
            #else:
            elif nums[mid] <= nums[-1]:
                #high moves mid
                high = mid
        #return nums[high]
        return nums[high]