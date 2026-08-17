class Solution:
    def isPalindrome(self, s: str) -> bool:
        #start a pointer in the left and right
        l, r = 0, len(s) - 1

        #loop until they meet or l goes past r
        while l < r:

            #if the current character is not alphanumeric move the pointer
            #ensure we stay in bounds
            while l < r and not s[l].isalnum():
                l += 1
            while r >l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True