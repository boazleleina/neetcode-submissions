class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "".join(str(len(item))+"#"+item for item in strs)
        return result
    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            #find the index of the next #
            next_sub = s.find("#", i)
            #parse the length from s[i:j] where j is where # is
            length = int(s[i:next_sub])
            #substring starts at j+1 and ends at j+1+length
            substring = s[next_sub+1:next_sub+1+length]
            #append results
            results.append(substring)
            #advance i to the new j position
            i = next_sub+1+length
        return results
