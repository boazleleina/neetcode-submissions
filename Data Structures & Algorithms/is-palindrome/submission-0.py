class Solution:
    def isPalindrome(self, s: str) -> bool:
        #instantiate left and right pointers
        l ,r = 0, len(s) - 1

        #loop until l and r meet or r becomes less than right
        while l < r:
            # if item in the l pointer is not alphanum, move pointer right
            # ensure it doesn't go out of bounds
            while l<r and not s[l].isalnum():
                l +=1
            #if item in r pointer is not alphanum, move pointer left
            #ensure it doesn't go out of bounds
            while r>l and not s[r].isalnum():
                r -= 1
            #if they are not equal exit loop immediately
            if s[l].lower() != s[r].lower():
                return False
            #move l up
            l += 1
            #move r down
            r -= 1
        return True


