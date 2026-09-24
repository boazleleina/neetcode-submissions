class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtracking(start):
            if start == len(s):
                res.append(curr.copy())
                return
            for end in range(start+1, len(s)+1):
                st = s[start:end]
                if not self._palindrome(st):
                    continue
                curr.append(s[start:end])
                backtracking(end)
                curr.pop()

        backtracking(0)
        return res
    
    def _palindrome(self, st):
        return st == st[::-1]
                