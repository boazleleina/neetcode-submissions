class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using QuickSelect

        #find where k would be in a sorted array
        k = len(nums) - k

        l,r = 0, len(nums)-1
        
        while True:
            pivot, p = nums[r], l

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1

            nums[r], nums[p] = nums[p], nums[r]

            if p < k:
                l = p+1
            elif p > k:
                r = p-1
            else:
                return nums[p]