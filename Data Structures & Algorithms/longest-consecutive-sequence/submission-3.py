class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #starting at [100,4,200,1,3,2,4]

        #becomes (1,2,3,4,100,200)
        num_set = set(nums)
        #instantiate the length
        longest = 0
        #loop through the set
        for num in num_set:
            #looking at 1, 0 is not in the num_set, so it's start of loop
            if num-1 not in num_set:
                length = 1
                #check the next value if it's there then add to length
                #example 2 is there so add, then update longest
                while num+1 in num_set:
                    length += 1
                    num +=1
                longest = max(longest, length)
        return longest

