class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = 0, len(nums1)

        while left <= right:
            mid = (left+right) // 2

            i = half - mid

            Aleft = nums1[mid-1] if mid>0 else float("-inf")
            Bleft = nums2[i-1] if i>0 else float("-inf")
            Aright = nums1[mid] if mid<len(nums1) else float("inf")
            Bright = nums2[i] if i < len(nums2) else float("inf")

            if Aleft > Bright:
                right = mid - 1
            elif Bleft > Aright:
                left = mid + 1
            else:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
