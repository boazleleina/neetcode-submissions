class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()

            #up cells [r-1, c], ensure it doesn't fall off the grid
            if r-1 >= 0 and grid[r-1][c] == 2147483647:
                grid[r-1][c] = grid[r][c] + 1
                q.append((r-1, c))
            
            #down [r+1, c], ensure it is within range
            if r+1 < rows and grid[r+1][c] == 2147483647:
                grid[r+1][c] = grid[r][c] + 1
                q.append((r+1, c))
            
            #left [r, c-1], ensure it doesn't fall off the grid
            if c-1 >= 0 and grid[r][c-1] == 2147483647:
                grid[r][c-1] = grid[r][c] + 1
                q.append((r, c-1))
            
            #right [r, c+1], ensure it doesn't fall off the grid
            if c+1 < cols and grid[r][c+1] == 2147483647:
                grid[r][c+1] = grid[r][c] + 1
                q.append((r, c+1))
            

            