class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for ch in st:
                count[ord(ch) - ord("a")] += 1
            sublist[tuple(count)].append(st)
        return list(sublist.values())