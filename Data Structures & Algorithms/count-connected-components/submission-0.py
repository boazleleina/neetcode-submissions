class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adjacency list map
        adj_map = defaultdict(list)

        for node in edges:
            adj_map[node[0]].append(node[1])
            adj_map[node[1]].append(node[0])
        
        count = 0
        visited = set()

        def dfs(node):

            visited.add(node)

            for nei in adj_map[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        

        return count

