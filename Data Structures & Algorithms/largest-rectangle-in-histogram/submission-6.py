class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                hgt = heights[stack.pop()]

                right = i

                left = stack[-1] if stack else -1

                width = right - left - 1

                area = hgt * width

                max_area = max(max_area, area)
            stack.append(i)
        
        # the elements left in the stack need to be equated
        n = len(heights)

        while stack:
            idx = stack.pop()
            height = heights[idx]
            left = stack[-1] if stack else -1
            width = n - left - 1
            area = height * width
            max_area = max(area, max_area)

        return max_area