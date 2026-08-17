class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store the values in a set -> lookup is O(1)
        numSet = set(nums)

        #integer to keep track of the longest sequence
        bestLength = 0

        

        for num in numSet:
            if (num-1) not in numSet:
                #initialize a counter to increment
                counter = 1

                while (num+counter) in numSet:
                    counter +=1
            
                if counter > bestLength:
                    bestLength = counter

        return bestLength