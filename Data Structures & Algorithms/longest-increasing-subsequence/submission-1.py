import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #holds the small possible tail value of a subsequence
        sub = []

        #loop over the array
        for num in nums:
            #find the left index where num should be inserted
            idx = bisect.bisect_left(sub, num)

            #if num is greater than any element in sub added it to the end
            if idx == len(sub):
                sub.append(num)
            #otherwise replace the first element that is greater
            else:
                sub[idx] = num
        return len(sub)
        

