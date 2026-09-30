class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def mark_safe(r,c):
            if (0 <= r < rows) and (0 <= c < cols) and (board[r][c]=="O"):
                board[r][c] = "T"

                mark_safe(r-1, c)
                mark_safe(r+1, c)
                mark_safe(r, c-1)
                mark_safe(r, c+1)
        
        
        #run it on top and down edges
        for c in range(cols):
            #recurse through the top row
            mark_safe(0, c)
            #recurse through the bottom row
            mark_safe(rows-1, c)
        
        #run it on left and right edges
        for r in range(rows):
            #recurse through the left col
            mark_safe(r, 0)
            #recurse through the right col
            mark_safe(r, cols-1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"