class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(st)) + "#" + st for st in strs)
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            # example 5#Hello5#world
            #find first #
            next_step = s.find("#", i)
            #get the int before it, length of the word i.e 5
            length = int(s[i:next_step])
            #find the word, starts after # ends at length
            word = s[next_step+1:next_step+1+length]
            #append word to list
            decoded_list.append(word)
            #increment i
            i = next_step+1+length
        return decoded_list
