class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1 # -> if empty then it can contribute only once
        prev1 = 1 if s[0] != '0' else 0

        for i in range(2, len(s)+1):
            current = (prev1 if 1 <= int(s[i-1]) <= 9 else 0) + (prev2 if 10 <= int(s[i-2:i]) <= 26 else 0)

            prev2 = prev1
            prev1 = current
        
        return prev1