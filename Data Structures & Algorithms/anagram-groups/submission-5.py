class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create hashmap which is a dictionary of lists
        anagram_map = defaultdict(list)
        #loop through each word in given list
        for st in strs:
            #create a list that contains 26 items for character a..z
            count = [0] * 26

            #loop through each character in the word
            for ch in st:
                #count number of each character
                count[ord(ch) - ord("a")] +=1
            #convert to tuple which is immuttable
            anagram_map[tuple(count)].append(st)
        
        return list(anagram_map.values())
