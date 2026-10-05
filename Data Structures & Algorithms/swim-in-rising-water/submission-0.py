class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #create a minheap to keep track of the highest peak in the path
        path_peak = []

        #seed the minheap with the first cell 0,0 and its elevation
        heapq.heappush(path_peak, (grid[0][0], 0, 0))

        #a set to keep track of nodes I have already visited
        visited = set()

        while path_peak:
            elevation, row, col  = heapq.heappop(path_peak)

            if row == n-1 and col == n-1:
                return elevation

            #check that the cell hasn't been processed before checking its neighbors           
            if (row,col) not in visited:
                #check the four neighbors
                #Up r-1, col
                if row-1 >= 0:
                    heapq.heappush(path_peak,(max(grid[row-1][col], elevation), row-1, col))
                #check down r+1, col
                if row+1 < n:
                    heapq.heappush(path_peak,(max(grid[row+1][col], elevation), row+1, col))
                #check left r, c-1
                if col-1 >= 0:
                    heapq.heappush(path_peak,(max(grid[row][col-1], elevation), row, col-1))
                #check right r, c+1
                if col+1 < n:
                    heapq.heappush(path_peak,(max(grid[row][col+1], elevation), row, col+1))
            visited.add((row,col))
            
