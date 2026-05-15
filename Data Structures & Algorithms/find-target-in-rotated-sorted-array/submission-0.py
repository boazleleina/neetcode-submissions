class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize low and high
        low, high = 0, len(nums)-1

        #while low is less than or equal to high:
        while low <= high:
            #calculate mid((low+high) // 2)
            mid = (low+high) // 2
            #if nums[mid] is the same as target:
            if nums[mid] == target:
                #return mid
                return mid
            #if nums[low] <= nums[mid] (means left side is sorted):
            if nums[low] <= nums[mid]:
                #check if nums[low] <= target <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    #high moves to mid-1
                    high = mid-1
                else:
                    #low move to mid+1
                    low = mid+1
            #else (means right side is sorted):
            else:
                #check if nums[mid] <= target <=nums[high]:
                if nums[mid] <= target <= nums[high]:
                    #low move to mid+1
                    low = mid + 1
                #else:
                else:
                    #high moves to mid-1
                    high = mid - 1
        #return -1
        return -1