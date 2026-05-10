class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initiate stack
        stack = []
        #initiate max_area
        max_area = 0

        #loop through indices in heights:
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                popped = stack.pop()
                height = heights[popped]
                right = i
                if not stack:
                    left = -1
                else:
                    left = stack[-1]
                width = right - left - 1
                area = height * width
                max_area = max(max_area, area)
            
            stack.append(i)

        n = len(heights)
        while stack:
            popped = stack.pop()
            height = heights[popped]
            right = n
            if not stack:
                left = -1
            else:
                left = stack[-1]
            width = right - left - 1
            area = height * width
            max_area= max(max_area, area)
        
        return max_area
