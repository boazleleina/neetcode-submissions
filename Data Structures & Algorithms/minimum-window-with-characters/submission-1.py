class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT, window = {} , {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        need = len(countT)
        
        best_length = float("inf")
        best_left = 0
        left, right = 0, 0
        have = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            while have == need:
                window_length = right-left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            
        if best_length == float("inf"):
            return ""
        return s[best_left : best_left + best_length]







