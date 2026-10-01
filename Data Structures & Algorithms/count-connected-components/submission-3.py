class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #using a union join
        #the nodes have a representative, the ones with the same representative count as connected component

        parent = list(range(n))
        count = n
        size = [1] * n
        
        
        def find(x):

            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
                
            if root_a != root_b:
                parent[root_b] = root_a
                return True
            return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                count -= 1
        
        return count


