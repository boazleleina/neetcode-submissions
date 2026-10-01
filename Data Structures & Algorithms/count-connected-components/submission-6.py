class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n))

        size = [1] * n

        count = n

        def find(x):
            
            while parent[x] != x :
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            #if they are already equal there's nothing to return
            if root_a == root_b:
                return False
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True
        
        for edge in edges:
            if union(edge[0], edge[1]):
                count -= 1
        
        return count

