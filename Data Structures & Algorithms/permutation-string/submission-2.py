class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check if the current length of s1 is greater than s2
        #if it is then return false since no window is valid
        if len(s1) > len(s2):
            return False


        #create an array to keep track of s1 character count
        s1_count = [0] * 26
        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1
        #create the initial window for s2, starting from 0 to length of s1
        window_count = [0]* 26
        for ch in s2[:len(s1)]:
            window_count[ord(ch)- ord("a")] += 1

        #check if the initial window is valid
        if window_count == s1_count:
            return True

        #loop through s2 using sliding window
        #r will move from len(s1) to len(s2):
        for r in range(len(s1), len(s2)):
            #enter the new character entering the window
            window_count[ord(s2[r]) - ord("a")] += 1
            #remove the first character in the window
            leav_ind = r - len(s1)
            window_count[ord(s2[leav_ind]) - ord("a")] -= 1
            #check if the current window is equal to s1 count
            if window_count == s1_count:
                return True
        #none of them are valid return False
        return False
