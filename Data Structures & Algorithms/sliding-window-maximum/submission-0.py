class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #instantiate tracker
        tracker = collections.deque()
        #instantiate output array
        output = []
        #loop through nums using r
        #for r in range(len(nums)):
        for r in range(len(nums)):
            #need to pop items from tracker
            # while tracker is not empty and nums[tracker[-1]] <= nums[r]:
            while tracker and nums[tracker[-1]] <= nums[r]:
                #pop items in the back of the tracker
                tracker.pop()
            #append r to tracker
            tracker.append(r)
            #check if the leftmost item in the tracker is still in the window
            #pop if it is not in the window
            if tracker[0] < r - k+ 1:
                #pop the left most element
                tracker.popleft()
            #check if the window is full before appending to output
            if r + 1 >= k:
                #append nums[tracker[0]] to output
                output.append(nums[tracker[0]])
        #return output
        return output