class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        countS = {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        need = len(countT)

        best_length = float("inf")
        have = 0
        best_left = 0
        l ,r = 0, 0

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                window_size = r - l+1

                if window_size < best_length:
                    best_length = window_size
                    best_left = l
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        if best_length == float("inf"):
            return ""
        return s[best_left : best_left+best_length]
