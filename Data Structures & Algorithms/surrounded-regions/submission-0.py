class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        def mark_safe(r,c):
            #check the safe regions and mark them
            if (0 <= r < rows) and (0 <= c < cols) and (board[r][c] == 'O'):
                board[r][c] = "T"
            
                #recurse for all up neighbors
                mark_safe(r-1, c)

                #recurse for all down neighbors
                mark_safe(r+1, c)

                #recurse left for all neighbors
                mark_safe(r, c-1)

                #recurse right to all neighbors
                mark_safe(r, c+1)
        
        for c in range(cols):
            #top row
            mark_safe(0, c)
            #bottom row
            mark_safe(rows-1, c)
        
        for r in range(rows):
            #left column
            mark_safe(r, 0)
            #right column
            mark_safe(r, cols-1)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
                
                
            
