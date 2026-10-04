class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #create an array to hold the weights and edges between each index
        edges = []
        #find the distance between each edge in the array
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((w,i,j))
        
        parent = list(range(len(points)))
        
        #create a size for each node
        size = [1] * len(points)
        
        #will be sorted by weight (w)
        #edges look like [(4,0,1), (6,0,2)...] before sorting, after sorting smallest weight go first
        edges.sort()


        #using union-find, here we check if the nodes are already connected, making them part of the same component
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            #if the edge already exists then return False
            if root_i == root_j:
                return False
            
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i

            size[root_i] += size[root_j]

            return True
        
        #initiate the result variable that will be added
        total = 0
        #once I reach n-1 nodes then I am done
        count = 0
        #loop through the connected components adding weights
        for w, i, j in edges:
            #if the edges are connected
            if union(i,j):
                total += w
                count += 1
                if count == len(points)-1:
                    break
        return total
                


            

        
