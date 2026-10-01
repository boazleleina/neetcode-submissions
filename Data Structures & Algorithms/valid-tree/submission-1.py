class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #edges have to be exactly n-1
        if len(edges) != n-1:
            return False
        
        #create an adjacency list
        adj_map = defaultdict(list)

        #maps are undirected so they go both ways
        for node in edges:
            adj_map[node[0]].append(node[1])
            adj_map[node[1]].append(node[0])
        
        #create visited set to hold nodes I have already seen
        visited = set()

        def dfs(node):

            visited.add(node)

            for nei in adj_map[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            
        
        if n>0:
            dfs(0)
        
        return len(visited) == n
            

