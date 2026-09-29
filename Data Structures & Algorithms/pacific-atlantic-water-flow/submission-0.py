class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows,cols = len(heights), len(heights[0])

        def find_island(r,c, ocean_set):
            ocean_set.add((r,c))

            #run the check for up [r-1, c]
            if (
                (0  <= r-1 < rows  ) and 
                ((r-1,c) not in ocean_set) and 
                heights[r-1][c] >= heights[r][c]):
                #recurse into the neighbor
                find_island(r-1, c, ocean_set)
            
            #run the check on down [r+1, c]
            if (
                (0  <= r+1 < rows  ) and 
                ((r+1,c) not in ocean_set) and 
                heights[r+1][c] >= heights[r][c]):
                #recurse into the neighbor
                find_island(r+1, c, ocean_set)
            
            #run the check on left [r, c-1]
            if (
                (0  <= c-1 < cols  ) and 
                ((r,c-1) not in ocean_set) and 
                heights[r][c-1] >= heights[r][c]):
                #recurse into the neighbor
                find_island(r, c-1, ocean_set)
            
            #run the check on right [r, c+1]
            if (
                (0  <= c+1 < cols  ) and 
                ((r,c+1) not in ocean_set) and 
                heights[r][c+1] >= heights[r][c]):
                #recurse into the neighbor
                find_island(r, c+1, ocean_set)

        #run the check for each cell and add it to the respective cell
        #for pacific all of the first col(0) to len(rows)-1 and then all of the first row to len(col)-1
        #for atlantic it is the last row to the last column and the last column to the last row
        for c in range(cols):
            find_island(0, c, pacific) # -> pacific is top row
            find_island(rows-1, c, atlantic) #-> atlantic is bottom row
        
        for r in range(rows):
            find_island(r, 0, pacific) # -> pacific is first column
            find_island(r, cols-1, atlantic) # ->atlantic is right column
        
       
        return [[r,c] for r,c in pacific & atlantic]
