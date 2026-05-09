class Solution:
    def trap(self, height: List[int]) -> int:
        #check if array is empty and return zero
        if not height:
            return 0
        #instantiate left pointer
        l = 0
        #instantiate right pointer
        r = len(height) - 1
        #instantiate max_left
        max_left = height[l]
        #instantiate max_right
        max_right = height[r]
        #instantiate total
        total = 0
        #while loop for l < r:
        while l < r:
            #check if max_l is less than max_r:
            if max_left < max_right:
                #update the left pointer
                l += 1
                #find the max between height[l] and max_left and update max_left
                max_left = max(max_left, height[l])
                #increment total by taking the max_left and subtracting height[l]
                total += max_left - height[l]
            #check else where max_r is leff:
            else:
                #update the right pointer
                r -= 1
                #find the max between height[r] and max_right and update max_right
                max_right = max(max_right, height[r])
                #increment total by taking the max_right and subtracting height[r]
                total += max_right - height[r]
        return total