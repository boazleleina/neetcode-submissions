class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = 0, len(nums1) - 1

        while True:
            mid1 = (left+ right) // 2

            mid2 = half - mid1 - 2

            Aleft = nums1[mid1] if mid1 >= 0 else float("-inf")
            Aright = nums1[mid1+1] if (mid1+1) < len(nums1) else float("inf")
            Bleft = nums2[mid2] if mid2 >= 0 else float("-inf")
            Bright = nums2[mid2+1] if (mid2+1) < len(nums2) else float ("inf")

            if Aleft > Bright:
                right = mid1-1
            elif Bleft > Aright:
                left = mid1 + 1
            else:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)