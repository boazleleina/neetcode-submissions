class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+ len(nums2)
        half = (total+1) // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        low, high = 0, len(nums1)

        while True:
            i = (low+high) // 2
            j = half - i

            nums1Left = nums1[i-1] if i > 0 else float("-inf")
            nums1Right = nums1[i] if i < len(nums1) else float("inf")
            nums2Left = nums2[j-1] if j > 0 else float("-inf")
            nums2Right = nums2[j] if j < len(nums2) else float("inf")

            if nums1Left  > nums2Right:
                high = i - 1
            elif nums2Left > nums1Right:
                low = i+1
            else:
                if total % 2:
                    return max(nums1Left, nums2Left)
                else:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2

           