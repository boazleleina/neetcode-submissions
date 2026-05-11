class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initiate stack
        stack = []
        #initiate max_area
        max_area = 0
        #loop through heights:
        for i in range(len(heights)):
            #while stack is not empty and heights[i] <= heights[stack[-1]]:
            while stack and heights[i] <= heights[stack[-1]]:
                #pop the top item in stack
                hgt = heights[stack.pop()]
                #right = i
                right = i
                #left is stack[-1] unless stack is empty in which case is -1
                left = stack[-1] if stack else -1
                #width is right - left - 1
                width = right - left - 1
                #area is popped item * width
                area = hgt * width
                #max_area is the max(max_area, area)
                max_area = max(max_area, area)
            
            #stack.append(i)
            stack.append(i)
        
        #initiate n which is equal to length of heights
        n = len(heights)
        #while stack is not empty:
        while stack:
            #pop the top item, this is our height
            hgt = heights[stack.pop()]
            #left is stack[-1] unless stack is empty in which case is -1
            left = stack[-1] if stack else -1
            #width is n - left - 1
            width = n - left - 1
            #area is popped item * width
            area = hgt * width
            #max_area is max(max_area, area)
            max_area = max(max_area, area)

        #return max_area
        return max_area