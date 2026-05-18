class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Trace halfway
        #initiate the total
        total = len(nums1) + len(nums2)
        #find the half point of the two arrays
        half = total // 2
        #initiate pointer for nums1 and nums2
        i, j = 0, 0
        #initiate previous and current
        previous = 0
        current = 0
        #loop until you get to index half+1, since it is 0-indexed
        for _ in range(half + 1):
            previous = current
            if i == len(nums1):
                current = nums2[j]
                j += 1
            elif j == len(nums2):
                current = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                current = nums1[i]
                i+= 1
            else:
                current = nums2[j]
                j += 1
        if total % 2:
            return current
        return (previous + current) / 2
            
