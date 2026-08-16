class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += str(len(st)) + "#" + st

        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = s.find("#", i)
            L = int(s[i:j])
            word = s[j+1 : j+1+L]
            output.append(word)
            i = j+1+L
        return output

