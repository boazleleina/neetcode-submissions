class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #create an adjacency list to hold the edges
        dict_order = {c: set() for word in words for c in word}

        #get the edges with each adjacent word
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if w1 > w2 and w1[:len(w2)] == w2:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    dict_order[w1[j]].add(w2[j])
                    break
        
        #create visited set to hold the nodes I have already seen
        visited = set()

        #create safe set for the nodes that form acyclic edges
        safe = set()

        #an array to hold te final order
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
        
        for c in dict_order:
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])

            