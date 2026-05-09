class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for st in strs:
            count = [0] * 26 #hold values for a...z
            for ch in st:
                count[ord(ch) - ord("a")] += 1
            my_dict[tuple(count)].append(st)
        return list(my_dict.values())