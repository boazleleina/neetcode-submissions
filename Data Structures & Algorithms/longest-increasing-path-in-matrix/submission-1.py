class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #keep track of each cell and the count
        cache = {}

        def dfs(r, c):
            #check if the current row column in cache already
            if (r,c) in cache:
                return cache[(r,c)]
            
            #current cell has a count of 1
            final_count = 1 
            #recurse through the neighbors only if the row and column are in bound and greater
            #UP [r-1][c]
            if r-1 >= 0 and matrix[r-1][c] > matrix[r][c]:
                final_count = max(final_count, 1+dfs(r-1, c))
            #DOWN [r+1][c]
            if r+1 < len(matrix) and matrix[r+1][c] > matrix[r][c]:
                final_count = max(final_count,1+dfs(r+1, c))
            #LEFT [r][c-1]
            if c-1 >= 0 and matrix[r][c-1] > matrix[r][c]:
                final_count = max(final_count,1+dfs(r, c-1))
            #RIGHT [r][c+1]
            if c+1 < len(matrix[0]) and matrix[r][c+1] > matrix[r][c]:
                final_count = max(final_count,1+dfs(r, c+1))
            
            cache[(r,c)] = final_count

            return final_count
        
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r,c))
        return res
            

            
