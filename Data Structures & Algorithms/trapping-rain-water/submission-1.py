class Solution:
    def trap(self, height: List[int]) -> int:
        # PREFIX AND POSTFIX METHOD
        # #instantiate n
        # #tracing on example [0,1,0,2,1,0,1,3,2,1,2,1]
        # # n will be 12
        # n = len(height)
        # #if n was 0, but it's not
        # if n ==0:
        #     return 0
        # #do forward loop
        # #max_left will be an array of 12 zeros
        # max_left = [0] * n
        # #start from the first zero
        # max_left[0] = height[0]
        # #example 2 in index height[3]
        # for i in range(1,n):
        #     #check all the values left of height[3], including itself
        #     #here the answer will be 2 since it the highest
        #     max_left[i] = max(max_left[i-1], height[i])
        # #do backward loop
        # # same to left, 12 zero array
        # max_right = [0] * n
        # # start at the end of the array
        # max_right[n-1] = height[n-1]
        # #here we'll start the loop one value before the last value
        # #since the last value is also included and we need range to capture it
        # for i in range(n-2, -1,-1):
        #     #the highest value will be at height[7] which is 3
        #     max_right[i] = max(max_right[i+1], height[i])
        
        # #find the total
        # total = 0
        # for i in range(n):
        #     #between height[3] and height[7] find the min
        #     # in our example it will 2 as the min, which is the same as the height,
        #     #so the total will not change for this index since we add 0 
        #     water = min(max_left[i], max_right[i]) - height[i]
        #     total += water
        # return total

        #TWO POINTER METHOD
        
        if len(height) == 0:
            return 0
        l = 0
        r = len(height) -1
        max_l = height[l]
        max_r = height[r]
        total = 0
        while l < r:
            if max_l < max_r:
                l+=1
                water = max_l - height[l]
                if water > 0:
                    total += water
                max_l = max(max_l, height[l])
            else:
                r -= 1
                water = max_r - height[r]
                if water > 0:
                    total += water
                max_r = max(max_r, height[r])

        return total

                






