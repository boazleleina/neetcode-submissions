class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #check that len of s is greater than len of t
        #return empty string otherwise

        if len(s) < len (t):
            return ""

        #instantiate an empty t_count dict
        t_count = {}
        #loop through the string t and add to t_count
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        #instantiate need which is the count of distinct keys in t_count
        need = len(t_count)

        #instantiate left pointer to 0
        l = 0
        #instantiate best length to infinity(largest possible number)
        best_length = float("inf")
        #instantiate best_left starting at 0
        best_left = 0

        #instantiate window_count as an empty dictionary
        window_count = {}

        #instantiate have to 0
        have = 0

        #go through s using the right pointer
        for r in range(len(s)):
            #enter the current character at the right pointer to window_count
            window_count[s[r]] = window_count.get(s[r], 0) + 1

            #if loop- check if s[right] is in t_count
            # and window_count[s[right]] == t_count[s[right]]:
                #if it is have +=1
            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1

            #start the while loop checking while have==need:
            while have == need:
                #record the current best length and best left, using if comparison to window_length
                window_len = r - l+1
                if window_len < best_length:
                    best_length = window_len
                    best_left = l
                #remove s[left] from window
                window_count[s[l]] -= 1
                #check if the character in s[left] is in t_count 
                #and if it's count just went below t_count[s_left]:
                    #decrement have by 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                
                #move l+= 1
                l += 1
                
        #return s[l:l+current best length] unless best_length is still inf in which case return empty string
        if best_length == float("inf"):
            return ""
        return s[best_left: best_left+best_length]
