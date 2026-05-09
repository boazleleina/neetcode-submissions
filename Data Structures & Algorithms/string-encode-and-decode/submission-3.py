class Solution:

    def encode(self, strs: List[str]) -> str:
      return  "".join(str(len(st))+ "#" + st for st in strs)

    def decode(self, s: str) -> List[str]:
        next_iter = 0
        res = []
        i = 0
        while i< len(s):
            next_iter = s.find("#", i)
            length = int(s[i:next_iter])
            word = s[next_iter+1:next_iter+1+length]
            i = next_iter + 1 + length
            res.append(word)
        return res
        

