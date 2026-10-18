class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #create a hashmap of the last occurence of each character of the string
        last_occ = {}
        for i in range(len(s)):
            last_occ[s[i]] = i
        
        res = []

        start, end = 0, 0

        for i in range(len(s)):
            #get to the last occurence of the character, and assign it to end
            end = max(end, last_occ[s[i]])

            #check if we are current at that last index
            if i == end:
                partition = i - start+1
                res.append(partition)
                start = i + 1
        
        return res