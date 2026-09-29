class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        INF = 2147483647

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col))
        
        while q:
            r, c = q.popleft()

            #process up, [r-1,c]
            if r-1 >= 0 and grid[r-1][c] == INF:
                grid[r-1][c] = grid[r][c] + 1
                q.append((r-1,c))
            
            #process down, [r+1,c]
            if r+1 < rows and grid[r+1][c] == INF:
                grid[r+1][c] = grid[r][c] + 1
                q.append((r+1,c))
                
            #process left, [r,c-1]
            if c-1 >= 0 and grid[r][c-1] == INF:
                grid[r][c-1] = grid[r][c] + 1
                q.append((r,c-1))
            
            #process right, [r, c+1]
            if c+1 < cols and grid[r][c+1] == INF:
                grid[r][c+1] = grid[r][c] + 1
                q.append((r,c+1))