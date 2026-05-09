class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #instantiate left pointer
        l = 0
        #instantiate count hash map
        count = {}
        #instantiate max_len
        max_len = 0
        #loop through s using r pointer:
        for r in range(len(s)):
            #enter the current character in the right pointer into the hashmap
            count[s[r]] = count.get(s[r], 0) + 1
            #calculate window size by subtracting l plus 1 since it is zero indexed from current r
            window_size = r - l + 1
            #if window_size - max(count.values()) > k:
            if window_size - max(count.values()) > k:
                #decrement the count of the character at current left pointer
                count[s[l]] -= 1
                #update the left pointer to shring window
                l += 1
            #find the max_len by taking current max_len and position of our pointers and return max
            max_len = max(max_len, r - l+ 1)
        #return max_len
        return max_len