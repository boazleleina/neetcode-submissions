class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def flood(r,c):
            if (r<0) or (r >= rows) or (c<0) or (c>=cols) or ((r,c) in visited) or( grid[r][c] == 0):
                return 0
            
            visited.add((r,c))

            return 1 + flood(r-1, c) + flood(r+1, c) + flood(r, c-1) + flood(r, c+1)
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area, flood(row, col))
        
        return max_area