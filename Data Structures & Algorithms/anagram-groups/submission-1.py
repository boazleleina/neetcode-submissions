class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subdict = defaultdict(list)
        for st in strs:
            count = [0] * 26 #store the ascii for lowercase a...z
            for ch in st:
                count[ord(ch) - ord("a")] += 1
            subdict[tuple(count)].append(st)
        return list(subdict.values())