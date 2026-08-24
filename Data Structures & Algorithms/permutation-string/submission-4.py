class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26

        for s in s1:
            s1_count[ord(s) - ord("a")] += 1
        
        s2_count = [0] * 26


        #check if the first window is valid
        for s in s2[:len(s1)]:
            s2_count[ord(s) - ord("a")] += 1

        if s1_count == s2_count:
            return True
        
        for ch in range(len(s1), len(s2)):
            #character from right is added to the window
            s2_count[ord(s2[ch]) - ord("a")] += 1

            #character on the left is removed from the window
            s2_count[ord(s2[ch - len(s1)]) - ord("a")] -= 1

            if s1_count == s2_count:
                return True

        return False
