class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def _countPal(left, right):
            count = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        for i in range(len(s)):
            odd_string = _countPal(i, i)
            even_string = _countPal(i, i+1)

            total += odd_string + even_string
        
        return total