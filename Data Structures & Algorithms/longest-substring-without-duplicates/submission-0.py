class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #instantiate left pointer to 0
        left = 0
        #instantiate an empty set
        char_set = set()
        #instantiate max window we've seen to 0
        max_window = 0
        #use right to loop through the s
        for r in range(len(s)):
            #while the current value of r is in the string,
            #remove the value of left character in set
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1

            #enter the new value in the set
            char_set.add(s[r])
            #find the max between current len of set and max
            max_window = max(max_window, len(char_set))
        #return max
        return max_window