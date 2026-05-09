class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # instantiate our area
        max_area = 0
        #instantiate the pointer
        l = 0
        r = len(heights) - 1
        #while the pointers haven't met
        while l < r:
            #calculate the area
            area = (r-l) * min(heights[l], heights[r])
            #update max area
            max_area = max(max_area, area)

            #if the left pointer is smaller, move the pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return max_area
          
