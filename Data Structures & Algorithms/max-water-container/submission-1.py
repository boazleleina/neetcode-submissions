class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0, len(heights)-1

        max_water = 0

        while l < r:
            width = r - l

            if heights[l] <= heights[r]:
                #means left is the shorter one, volume is bounded by shorter height
                cur_vol = heights[l] * width
                max_water = max(cur_vol, max_water)
                l+=1
            else:
                cur_vol = heights[r] * width
                max_water = max(cur_vol, max_water)
                r -= 1
        return max_water