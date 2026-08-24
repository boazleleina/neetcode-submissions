class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        #use a hash set because lookup is O(1) and popping element is O(1)
        window = set()

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[i])
            max_length = max(max_length, len(window))

        return max_length
