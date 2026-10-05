class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #create the adjacency list to hold the edges, it needs to be seeded with the keys which is every unique character within the words array
        dict_order = {c: set() for word in words for c in word}

        

        #create the edges by looping through each word and adding it to the set
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    dict_order[w1[j]].add(w2[j])
                    break
        

        #need a visited node set, to ensure we are not in a cycle, if a node appears again then we hit a repeated edge and this makes the claim incorrect
        visited = set()

        #if the node can be reached in order, then we can return safe
        safe = set()

        #create an array to hold the final characters
        res = []

        def dfs(node):
            if node in visited:
                return False
            if node in safe:
                return True
            
            visited.add(node)

            for nei in dict_order[node]:
                if not dfs(nei):
                    return False
            
            safe.add(node)
            res.append(node)

            visited.remove(node)
            
            return True
        

        #loop through the dictionary to get the nodes to check against
        for c in dict_order:
            if not dfs(c):
                return ""
        return "".join(res[::-1])
        

            
            
                
                