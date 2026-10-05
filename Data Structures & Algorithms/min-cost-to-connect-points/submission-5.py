class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #an array edges to hold all the weights and points
        edges = []
        #find the manhattan distance between each node
        for i in range(n):
            for j in range(i+1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((w,i,j))
        #sort the edges by weight
        edges.sort()

        #create the parents array from 0-n
        parent = list(range(n))

        #create size array to hold the sizes of each root
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False

            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i

            size[root_i] += size[root_j]
            return True
        
        #keep track of total distance
        total = 0
        #track count to n-1 stop immediately when edges satisfy the count
        count = 0

        for w, i, j in edges:
            if union(i,j):
                total += w
                count += 1
                if count == n-1:
                    break
        
        return total

