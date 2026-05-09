class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check if s2>s1 to ensure there's an early exit
        if len(s1)>len(s2):
            return False

        #instantiate s1 into a list of the count of characters
        s1_count = [0]*26

        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1

        #instatiate window_count to keep count of s2 characters in the window
        window_count = [0]*26

        #check if the first window is valid
        for ch in s2[:len(s1)]:
            window_count[ord(ch) - ord("a")] += 1
        if window_count == s1_count:
            return True

        #loop through the next windows starting at len(s1)+1, ending at len(s2)
        for r in range(len(s1), len(s2)):

            #character from the right is added to the window
            window_count[ord(s2[r]) - ord("a")] += 1
            #first character on the left is removed
            window_count[ord(s2[r - len(s1)]) - ord("a")] -= 1

            #compare the new window_count to s1_count
            if window_count == s1_count:
                #return True if a permutation is found
                return True

        #return False if no permutation is found
        return False
