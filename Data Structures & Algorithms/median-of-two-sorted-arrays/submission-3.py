class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Binary search
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = (total+1) // 2

        l, h = 0, len(nums1)

        while True:
            i = (l+h) // 2
            j = half - i

            Aleft = nums1[i-1] if i>0 else float("-inf")
            Bleft = nums2[j-1] if j>0 else float ("-inf")
            Aright = nums1[i] if i < len(nums1) else float("inf")
            Bright = nums2[j] if j < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return max(Aleft, Bleft)
                return (min(Aright,Bright) + max(Aleft, Bleft)) /2
            #too many values from left
            elif Aleft > Bright:
                h = i-1
            else:
                l = i+1
                 


     
            
