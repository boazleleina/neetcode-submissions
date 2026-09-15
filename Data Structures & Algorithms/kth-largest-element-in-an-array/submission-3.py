class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using QuickSelect

        #find where k would be in a sorted array
        k = len(nums) - k

        def QuickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                return QuickSelect(p+1, r)
            elif p > k:
                return QuickSelect(l, p-1)
            else:
                return nums[p]
        
        return QuickSelect(0, len(nums)-1)