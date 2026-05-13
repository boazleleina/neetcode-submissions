class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize left and right
        left, right = 0, len(nums) - 1

        #loop through the array, while left <= right:
        while left <= right:
            #calculate the middle value
            middle = (left+right) // 2
            #check if nums[middle] == target:
            if nums[middle] == target:
                # return middle
                return middle
            #else if nums[middle] < target:
            elif nums[middle] < target:
                #left is updated
                left = middle+1
            #else if nums[middle] > target:
            else:
                #right is updated
                right = middle-1
        #return -1, the loop ran and target was never found
        return -1