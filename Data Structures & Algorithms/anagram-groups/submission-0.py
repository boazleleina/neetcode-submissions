class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = defaultdict(list)
        for item in strs:
            count = [0] * 26 #a...z ascii mapping
            for char in item:
                count[ord(char) - ord("a")] += 1
            my_hash[tuple(count)].append(item)
        return list(my_hash.values())
