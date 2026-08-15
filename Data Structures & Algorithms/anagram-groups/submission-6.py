class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create the hashmap to hold the sublists- will be a dictionary of lists
        chr_list = defaultdict(list)

        #loop through the strs array and convert each strs to an integer equivalent

        for wrd in strs:
            #I need the key, create a list of 26 values of the alphabet
            count = [0] * 26

            for ch in wrd:
                #convert characters to integer equivalent, and add them to the list
                count[ord(ch) - ord("a")] += 1

            #append the count to the hashmap
            #list is immutable, so convert to tuple

            chr_list[tuple(count)].append(wrd)

        return list(chr_list.values())