class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def _findPalindrome(left, right):
            while (left >= 0) and (right < len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        for i in range(len(s)):
            odd_string = _findPalindrome(i, i)
            even_string = _findPalindrome(i, i+1)

            res = max(res, odd_string, even_string, key=len)
        return res
