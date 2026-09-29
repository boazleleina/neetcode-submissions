class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #queue to keep track of each level
        q = collections.deque()
        fresh_count = 0
        minutes = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                #process up neighbor
                if r-1 >= 0 and grid[r-1][c] == 1:
                    #rot the neighbor
                    grid[r-1][c] = 2
                    #fresh_count is decremented
                    fresh_count -= 1
                    #append the neighbor to the queue
                    q.append((r-1,c))
                
                #process down neighbor
                if r+1 < rows and grid[r+1][c] == 1:
                    #rot the neighbor
                    grid[r+1][c] = 2
                    #fresh_count is decremented
                    fresh_count -= 1
                    #append the neighbor to the queue
                    q.append((r+1,c))
                
                #process left neighbor
                if c-1 >= 0 and grid[r][c-1] == 1:
                    #rot the neighbor
                    grid[r][c-1] = 2
                    #fresh_count is decremented
                    fresh_count -= 1
                    #append the neighbor to the queue
                    q.append((r,c-1))
                
                #process right neighbor
                if c+1 < cols and grid[r][c+1] == 1:
                    #rot the neighbor
                    grid[r][c+1] = 2
                    #fresh_count is decremented
                    fresh_count -= 1
                    #append the neighbor to the queue
                    q.append((r,c+1))
            minutes += 1
        
        if fresh_count>0:
            return -1
        else:
            return minutes
                
                
                
